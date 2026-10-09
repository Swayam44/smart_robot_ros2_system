#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryNode(Node):
    def __init__(self):
        super().__init__('battery_node')
        self.publisher_ = self.create_publisher(Float32, '/battery_status', 10)
        self.timer_ = self.create_timer(1.0, self.publish_battery)
        self.battery_level = 99.8
        self.get_logger().info('Battery node started.')

    def publish_battery(self):
        if self.battery_level > 0.0:
            self.battery_level = max(0.0, self.battery_level - 0.2)

        msg = Float32()
        msg.data = float(self.battery_level)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Battery: {msg.data:.1f}%')


def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
