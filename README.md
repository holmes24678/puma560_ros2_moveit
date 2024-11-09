
# PUMA560 Robot Manipulation using ROS2 and Moveit2

This Github repository demonstrates simulation of PUMA560 robot Manipulation using ROS2 and Moveit2.

#### Hey there, i am enthuastic robotics guy. my interest in robotics begin when i watched ironman (respect for Tony stark). if you like my content and any colloborates needed please feel to reach me at hsherlock366@gmail.com

### To test this project follow the below steps

## 1. Install Prerequisites
### ROS2 humble

https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html

### ROS2 Jazzy

https://docs.ros.org/en/jazzy/Installation.html

### Install Moveit2

https://moveit.ai/install-moveit2/binary/

### Install Gazebosim

https://gazebosim.org/docs/latest/getstarted/

(check for compatiable version for your $ROS_DISTRO)

## 2. Clone the repository
```
git clone https://github.com/holmes24678/puma560_ros2_moveit.git
```
## 3. Build the workspace using colcon
```
colcon build 
```
## 4. Launch the gazebo.launch py
```
ros2 launch puma560_description gazebo.launch.py
```
### you will output as
## 5. Launch the controllers.launch.py. this will launch the gazebo simulation
```
ros2 launch puma560_description controllers.launch.py. This will activate the controllers
```
## 6. Launch the execute.launch.py. This will plan and execute the trajectory for the required goal pose
```
ros2 launch puma560_description execute.launch.py
```

