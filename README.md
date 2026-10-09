# Smart Robot ROS 2 System

A ROS 2 based modular robot communication system designed to demonstrate sensor processing, robot decision-making, battery monitoring, service-based control, and centralized visualization in a beginner-friendly architecture.

## Project Overview

This project simulates a robot system built using ROS 2 Humble on Ubuntu 22.04. It demonstrates how multiple independent nodes communicate through topics, services, parameters, and launch files to form a compact but realistic robot control architecture.

The repository is intentionally structured to be easy to understand for students and robotics engineers who are learning the fundamentals of ROS 2 communication.

## Features

- Distance sensor simulation using a ROS 2 publisher node
- Robot decision logic for safe vs. blocked motion
- Battery monitoring with decreasing battery levels
- Robot state management and status reporting
- Service-based robot start/stop control
- Central dashboard node for live robot monitoring
- Launch-based startup for the full robot system
- Beginner-friendly Python implementation for ROS 2

## System Architecture

```text
                    robot_system.launch.py
                             |
        ------------------------------------------------
        |                 |              |              |
        v                 v              v              v

   Sensor Node      Controller Node   Battery Node   Monitor Node
       |                 |              |              |
       |                 |              |              |
       v                 v              v              v

   /sensor_data      /robot_status   /battery_status    Dashboard
       |                 |              |              |
       +-----------------+--------------+--------------+
                             |
                             v
                    Robot Monitoring System
```

## ROS 2 Concepts Demonstrated

- Nodes
- Topics and message publishing/subscribing
- Services for remote commands
- Parameters and runtime configuration
- Launch files for system startup
- Multi-node architecture in a realistic robotics workflow

## Repository Structure

```text
smart_robot_ros2_system/
├── smart_robot/
│   ├── launch/
│   │   └── robot_system.launch.py
│   ├── smart_robot/
│   │   ├── __init__.py
│   │   ├── sensor_node.py
│   │   ├── controller_node.py
│   │   ├── battery_node.py
│   │   ├── monitor_node.py
│   │   └── control_node.py
│   ├── package.xml
│   ├── setup.py
│   └── setup.cfg
├── docs/
│   └── architecture_diagram.md
├── README.md
├── .gitignore
├── LICENSE
└── screenshots/
    └── README.md
```

## Hardware and Software Requirements

### Hardware

- Computer running Ubuntu 22.04 LTS
- Minimum 8 GB RAM recommended
- A desktop or laptop capable of running ROS 2 Humble

### Software

- Ubuntu 22.04 LTS
- ROS 2 Humble Hawksbill
- Python 3.10+
- colcon build tools
- git

## ROS 2 Dependencies

This project uses the following packages:

- rclpy
- std_msgs
- std_srvs
- launch
- launch_ros

## Installation

### 1. Create a ROS 2 workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

### 2. Clone the repository

```bash
git clone https://github.com/Swayam44/smart_robot_ros2_system.git
```

### 3. Install dependencies

```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```

If you do not have rosdep initialized yet, do this first:

```bash
sudo apt update
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
```

## Build Instructions

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
```

## Source the Workspace

```bash
source ~/ros2_ws/install/setup.bash
```

## Run the Project

Launch the entire robot system:

```bash
ros2 launch smart_robot robot_system.launch.py
```

This command starts:

- Sensor node
- Controller node
- Battery monitoring node
- Dashboard monitor node
- Robot control service server

## Example ROS 2 Commands

### View active topics

```bash
ros2 topic list
```

### Monitor sensor data

```bash
ros2 topic echo /sensor_data
```

### Monitor robot status

```bash
ros2 topic echo /robot_status
```

### Monitor battery percentage

```bash
ros2 topic echo /battery_status
```

### Start the robot using service call

```bash
ros2 service call /robot_control std_srvs/srv/SetBool "{data: true}"
```

### Stop the robot using service call

```bash
ros2 service call /robot_control std_srvs/srv/SetBool "{data: false}"
```

## Expected Dashboard Output

```text
========================
     ROBOT DASHBOARD
========================
SYSTEM      : ONLINE
Robot State : IDLE
Distance    : 3.50 m
Movement    : MOVE - Path clear
Battery     : 99.8 %
========================
```

## Screenshot / GIF Placeholder

Add your dashboard screenshot or demo GIF here:

- Dashboard output screenshot: `screenshots/dashboard_output.png`
- Demo video/GIF: `screenshots/robot_demo.gif`

You can replace these placeholder locations with real project images before publishing your portfolio.

## Troubleshooting

### 1. Package not found

If ROS 2 cannot find the package, make sure the workspace is sourced:

```bash
source ~/ros2_ws/install/setup.bash
```

### 2. Build fails

Try cleaning the workspace and rebuilding:

```bash
cd ~/ros2_ws
rm -rf build install log
colcon build --symlink-install
```

### 3. Topics not publishing

Check if the launch file started correctly:

```bash
ros2 node list
ros2 topic list
```

### 4. Service not responding

Verify the service exists:

```bash
ros2 service list | grep robot_control
```

## Future Improvements

- Add ROS 2 actions for autonomous robot missions
- Add TF2 coordinate transformation support
- Add URDF robot model for visualization
- Add RViz monitoring interface
- Add Gazebo simulation environment
- Integrate real hardware robot controllers
- Add navigation stack integration for autonomous movement

## Professional Git Commit Suggestions

Use clear and meaningful commit messages like:

```bash
git commit -m "Initialize ROS 2 smart robot communication framework"
git commit -m "Add sensor publisher node"
git commit -m "Implement robot controller logic"
git commit -m "Add battery monitoring node"
git commit -m "Create centralized robot dashboard"
git commit -m "Add ROS 2 launch system"
git commit -m "Update project documentation and architecture diagram"
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

GitHub: Swayam44

## Portfolio Note

This repository is designed to be clean, modular, and understandable for robotics engineering learners and portfolio reviewers. It demonstrates practical ROS 2 communication patterns in a compact, real-world-inspired robot architecture.

If you want to extend this project further, consider adding Gazebo simulation, RViz visualization, or a real mobile robot integration layer.
