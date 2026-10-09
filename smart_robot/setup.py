from setuptools import setup

package_name = 'smart_robot'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    package_dir={'': '.'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Swayam44',
    maintainer_email='your_email@example.com',
    description='ROS 2 modular robot communication system',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_node = smart_robot.sensor_node:main',
            'controller_node = smart_robot.controller_node:main',
            'battery_node = smart_robot.battery_node:main',
            'monitor_node = smart_robot.monitor_node:main',
            'robot_control_service = smart_robot.control_node:main',
        ],
    },
)
