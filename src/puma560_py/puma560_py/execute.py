import time
import numpy as np
import rclpy
from rclpy.logging import get_logger

from moveit.core.robot_state import RobotState
from moveit.planning import MoveItPy
from moveit.core.kinematic_constraints import construct_joint_constraint

def plan_and_execute(robot,
                    planning_component,
                    logger,
                    single_plan_parameters=None,
                    multi_plan_parameters=None,
                    sleep_time= 0.0,):
                    
                    logger.info("Planning Trjectory")
                    if multi_plan_parameters is not None:
                        plan_result = planning_component.plan(
                            multi_plan_parameters = multi_plan_parameters
                        )
                    elif single_plan_parameters is not None:
                        plan_result = planning_component.plan(
                            single_plan_parameters =single_plan_parameters
                        )
                    else:
                        plan_result = planning_component.plan()

                    if plan_result:
                        logger.info("Executing plan")
                        robot_trajectory = plan_result.trajectory
                        robot.execute(robot_trajectory, controllers = [])
                    else:
                        logger.error("Planning failed")
                    
                    time.sleep(sleep_time)

def main():
    rclpy.init()
    logger = get_logger("moveit_py.pose_goal")
    puma = MoveItPy(node_name = "moveit_py")
    puma_arm1 = puma.get_planning_component("arm")
    puma_arm2 = puma.get_planning_component("arm")
    puma_arm3 = puma.get_planning_component("arm")
    puma_arm4 = puma.get_planning_component("arm")
    logger.info("MoveItPy instance created")

    robot_model = puma.get_robot_model()
    arm_state1 = RobotState(robot_model)
    arm_state2 = RobotState(robot_model)
    arm_state3 = RobotState(robot_model)
    arm_state4 = RobotState(robot_model)
  
    puma_arm1.set_start_state_to_current_state()
    puma_arm2.set_start_state_to_current_state()
    puma_arm3.set_start_state_to_current_state()
    puma_arm4.set_start_state_to_current_state()
   
    
    arm_state1.set_joint_group_positions("arm", np.array([1.57, 0.0, 0.0,0,0,0]))
    arm_state2.set_joint_group_positions("arm", np.array([1.57, 0.7, 0.0,0,0,0]))
    arm_state3.set_joint_group_positions("arm", np.array([1.57, 0.7, 0.7,0,0,0]))
    arm_state4.set_joint_group_positions("arm", np.array([0, 0.0, 0.0,0,0,0]))

    puma_arm1.set_goal_state(robot_state = arm_state1)
    puma_arm2.set_goal_state(robot_state = arm_state2)
    puma_arm3.set_goal_state(robot_state = arm_state3)
    puma_arm4.set_goal_state(robot_state = arm_state4)


    plan_and_execute(puma,puma_arm1,logger,sleep_time=3.0)
    plan_and_execute(puma,puma_arm2,logger,sleep_time=3.0)
    plan_and_execute(puma,puma_arm3,logger,sleep_time=3.0)
    plan_and_execute(puma,puma_arm4,logger,sleep_time=3.0)



if __name__ == "__main__":
      main()
