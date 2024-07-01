# This is a repo to facilitate the use of Intel RealSense D400 Series cameras everywhere in the world

This repo is tested only on Intel RealSense D455 camera and Ubutnu 22.04.

## Before to Start
Be sure that Intel RealSense SDK 2.0 is installed:

```
sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils
```

(please refer to: https://github.com/IntelRealSense/librealsense/blob/development/doc/distribution_linux.md)

Be sure that the ros2 wrapper is installed (here we will refere always to ROS2 Humble):

```
sudo apt install ros-humble-librealsense2*
sudo apt install ros-humble-realsense2-camera
```

(please refer to: https://github.com/IntelRealSense/realsense-ros (ros2-development branch))

IMPORTANT: be sure to calibrate your camera and save the parameters on-board (using realsense-viewer) or somewhere else.
In the latter case you will not have useful information in the camera_info topic of the recorded bag.

If you want to use ROS2 camera calib refer to this link:
https://docs.nav2.org/tutorials/docs/camera_calibration.html

It is preferable to use the Intel RealSense D400 Series Dynamic Calibration Tool:
https://www.intel.com/content/www/us/en/download/645988/intel-realsense-d400-series-dynamic-calibration-tool.html

On Ubuntu you need to install the software following the instruction in the link above and then run the executable "Inter.RealSense.DynamicCalibrator" installed at "/usr/bin/".



## How to use me
If you installed everything you just need to start the recording with:

```
ros2 launch launch/record_bag.launch.py output_folder:="/path/where/you/want/your/bag/to/be/saved/"
```

and press CTRL-C when you are done.

Then, you can use this command to extract the images:

```
python3 extract_images.py /path/of/the/bag/folder/ /path/where/you/want/your/images/
```
