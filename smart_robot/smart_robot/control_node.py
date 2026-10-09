#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import SetBool


class RobotControlService(Node):
    def __init__(self):
        super().__init__('robot_control_service')
        self.service_ = self.create_service(SetBool, '/robot_control', self.handle_robot_control)
        self.state_publisher_ = self.create_publisher(String, '/robot_state', 10)
        self.robot_active = True
        self.get_logger().info('Robot control service started.')

    def handle_robot_control(self, request, response):
        self.robot_active = request.data
        state = 'ACTIVE' if self.robot_active else 'IDLE'
        state_msg = String()
        state_msg.data = state
        self.state_publisher_.publish(state_msg)

        response.success = True
        response.message = 'Robot started.' if self.robot_active else 'Robot stopped.'
        self.get_logger().info(f'Received control request: {request.data}')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = RobotControlService()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
