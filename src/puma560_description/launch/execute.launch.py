import os
from launch import LaunchDescription
from moveit_configs_utils import MoveItConfigsBuilder
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("puma560", package_name="puma560_description")
        .robot_description(file_path="urdf/puma560_robot.urdf")
        .robot_description_semantic(file_path="config/puma560.srdf")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .moveit_cpp(file_path="config/planning.yaml")
        .to_moveit_configs()
    )
    launch_node = Node(
        package="puma560_py",
        executable="execute",
        parameters= [moveit_config.to_dict(),
                     {'use_sim_time' : True}]
    )

    return LaunchDescription([
        launch_node,
    ])