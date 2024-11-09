
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
### 4. ## 4. Launch the display.launch py
```
ros2 launch puma560_description display.launch.py
```
### you will get output as
![display](https://github.com/user-attachments/assets/2ad145fc-836e-4079-98cf-d9023d761476)
## 4. Launch the gazebo.launch py
```
ros2 launch puma560_description gazebo.launch.py
```
### you will get output as
![gazebo](https://github.com/user-attachments/assets/874b1e29-bb5b-445d-a772-1bd3b45f61ae)
## 5. Launch the command.launch.py. this will launch the gazebo simulation with controllers activated
```
ros2 launch puma560_description controllers.launch.py. This will activate the controllers
```
### 6. Launch the moveit.launch.py. This will launch moveit planning plugin in RVIZ
```
ros2 launch puma560_description moveit.launch.py
```
### You will get output as 
![moveit](https://github.com/user-attachments/assets/4596d65b-dda5-4371-a124-e71081088543)

## 6. Launch the execute.launch.py. This will plan and execute the trajectory for the required goal pose
```
ros2 launch puma560_description execute.launch.py
```
### You will get output as
![video-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/67f96dbd-8598-4789-94ab-f9166c23e7de)

Thanks for coming!. Have a nice Day

