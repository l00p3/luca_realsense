from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution


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
                }.items(),
            ),
            ExecuteProcess(
                cmd=[
                    "ros2",
                    "run",
                    "camera_calibration",
                    "cameracalibrator",
                    "--size 9x6",
                    "--square 0.023",
                    "--ros-args",
                    "-r",
                    "image:=/camera/camera/color/image_raw",
                    "-p",
                    "camera:=/camera",
                ],
                shell=True,
            ),
        ],
    )
