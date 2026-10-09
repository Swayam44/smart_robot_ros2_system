#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class MonitorNode(Node):
    def __init__(self):
        super().__init__('monitor_node')
        self.sensor_sub_ = self.create_subscription(Float32, '/sensor_data', self.sensor_callback, 10)
        self.status_sub_ = self.create_subscription(String, '/robot_status', self.status_callback, 10)
        self.state_sub_ = self.create_subscription(String, '/robot_state', self.state_callback, 10)
        self.battery_sub_ = self.create_subscription(Float32, '/battery_status', self.battery_callback, 10)

        self.current_distance = 0.0
        self.current_status = 'UNKNOWN'
        self.current_state = 'IDLE'
        self.current_battery = 0.0
        self.get_logger().info('Monitor dashboard started.')
        self.print_dashboard()

    def sensor_callback(self, msg):
        self.current_distance = float(msg.data)
        self.print_dashboard()

    def status_callback(self, msg):
        self.current_status = msg.data
        self.print_dashboard()

    def state_callback(self, msg):
        self.current_state = msg.data
        self.print_dashboard()

    def battery_callback(self, msg):
        self.current_battery = float(msg.data)
        self.print_dashboard()

    def print_dashboard(self):
        print('\n========================')
        print('     ROBOT DASHBOARD')
        print('========================')
        print(f'SYSTEM      : ONLINE')
        print(f'Robot State : {self.current_state}')
        print(f'Distance    : {self.current_distance:.2f} m')
        print(f'Movement    : {self.current_status}')
        print(f'Battery     : {self.current_battery:.1f} %')
        print('========================\n')


def main(args=None):
    rclpy.init(args=args)
    node = MonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
