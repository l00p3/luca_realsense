from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [
                        PathJoinSubstitution(
                            [
                                FindPackageShare("realsense2_camera"),
                                "launch",
                                "rs_launch.py",
                            ]
                        )
                    ]
                ),
                launch_arguments={
                    "config_file": "config.yaml",
                    "output": "screen",
                }.items(),
            ),
            ExecuteProcess(
                cmd=[
                    "ros2",
                    "bag",
                    "record",
                    "/camera/camera/color/camera_info",
                    "/camera/camera/color/image_raw",
                    "/camera/camera/aligned_depth_to_color/camera_info",
                    "/camera/camera/aligned_depth_to_color/image_raw",
                ],
                output="screen",
            ),
        ],
    )
