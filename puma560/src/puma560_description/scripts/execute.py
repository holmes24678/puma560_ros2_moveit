import rclpy
from rclpy.logging import get_logger
from moveit.planning import MoveItPy
from moveit.core.robot_state import RobotState
import numpy as np
import time

def execute():
    #creating moveit object
    puma560_robot = MoveItPy(node_name = "moveit_py")
    #defining robot arm as planning component
    puma560_robot_arm = puma560_robot.get_planning_component("arm")
    arm_state = RobotState(puma560_robot.get_robot_model())
    #setting joint angles positions
    #solve inverse kinematics for your required joint
    arm_state.set_joint_group_positions("arm", np.array([1,1.9,0,0,1.57,1]))

    puma560_robot_arm.set_start_state_to_current_state()

    puma560_robot_arm.set_goal_state(robot_state = arm_state)

    arm_plan_result = puma560_robot_arm.plan()

    if arm_plan_result:
        puma560_robot.execute(arm_plan_result.trajectory, controllers = [])
    else:
        get_logger("rclpy").error("planners failed to execute")

def execute1():
    #creating moveit object
    puma560_robot = MoveItPy(node_name = "moveit_py")
    #defining robot arm as planning component
    puma560_robot_arm = puma560_robot.get_planning_component("arm")
    arm_state = RobotState(puma560_robot.get_robot_model())
    #setting joint angles positions
    #solve inverse kinematics for your required joint
    arm_state.set_joint_group_positions("arm", np.array([0,0,0,0,1.57,1]))

    puma560_robot_arm.set_start_state_to_current_state()

    puma560_robot_arm.set_goal_state(robot_state = arm_state)

    arm_plan_result = puma560_robot_arm.plan()

    if arm_plan_result:
        puma560_robot.execute(arm_plan_result.trajectory, controllers = [])
    else:
        get_logger("rclpy").error("planners failed to execute") 

def main():
    rclpy.init()
    execute()
    time.sleep(2)
    execute1()
    rclpy.shutdown()


if __name__ == "__main__":
    main()