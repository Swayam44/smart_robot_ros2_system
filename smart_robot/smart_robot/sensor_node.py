#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(Float32, '/sensor_data', 10)
        self.timer_ = self.create_timer(1.0, self.publish_distance)
        self.get_logger().info('Sensor node started.')
        self.distance = 5.0

    def publish_distance(self):
        self.distance = max(0.5, self.distance - 0.15)
        if self.distance <= 0.8:
            self.distance = 5.0

        msg = Float32()
        msg.data = float(self.distance)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published distance: {msg.data:.2f} m')


def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
