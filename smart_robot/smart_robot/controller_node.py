#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.subscriber_ = self.create_subscription(Float32, '/sensor_data', self.sensor_callback, 10)
        self.publisher_ = self.create_publisher(String, '/robot_status', 10)
        self.state_publisher_ = self.create_publisher(String, '/robot_state', 10)
        self.robot_active = True
        self.last_distance = 0.0
        self.get_logger().info('Controller node started.')

    def sensor_callback(self, msg):
        self.last_distance = float(msg.data)
        if self.robot_active:
            if self.last_distance > 1.5:
                status = 'MOVE - Path clear'
                state = 'MOVING'
            else:
                status = 'STOP - Obstacle detected'
                state = 'STOPPED'
        else:
            status = 'STOP - Robot manually stopped'
            state = 'IDLE'

        status_msg = String()
        status_msg.data = status
        self.publisher_.publish(status_msg)

        state_msg = String()
        state_msg.data = state
        self.state_publisher_.publish(state_msg)

        self.get_logger().info(f'Distance: {self.last_distance:.2f} m | {status}')

    def set_robot_active(self, active):
        self.robot_active = bool(active)
        if not self.robot_active:
            self.get_logger().info('Robot stopped by service command.')
        else:
            self.get_logger().info('Robot started by service command.')


def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
