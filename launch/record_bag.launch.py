from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    ExecuteProcess,
    DeclareLaunchArgument,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    output_folder = LaunchConfiguration("output_folder")
    output_bag_name = DeclareLaunchArgument("output_folder", default_value="kitemurt")

    return LaunchDescription(
        [
            output_bag_name,
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
                    "-o",
                    output_folder,
                ],
                shell=True,
            ),
            ExecuteProcess(
                cmd=[
                    "ros2",
                    "run",
                    "rqt_image_view",
                    "rqt_image_view",
                    "/camera/camera/color/image_raw",
                ],
            ),
        ],
    )
