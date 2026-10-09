from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='smart_robot',
            executable='sensor_node',
            name='sensor_node',
            output='screen'
        ),
        Node(
            package='smart_robot',
            executable='controller_node',
            name='controller_node',
            output='screen'
        ),
        Node(
            package='smart_robot',
            executable='battery_node',
            name='battery_node',
            output='screen'
        ),
        Node(
            package='smart_robot',
            executable='monitor_node',
            name='monitor_node',
            output='screen'
        ),
        Node(
            package='smart_robot',
            executable='robot_control_service',
            name='robot_control_service',
            output='screen'
        ),
    ])
