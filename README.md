# This is a repo to facilitate the use of RealSense cameras everywhere in the world

## Before to Start
Be sure that Intel RealSense SDK 2.0 is installed:

sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils

(please refer to: https://github.com/IntelRealSense/librealsense/blob/development/doc/distribution_linux.md)

Be sure that the ros2 wrapper is installed (here we will refere always to ROS2 Humble):

sudo apt install ros-humble-librealsense2*
sudo apt install ros-humble-realsense2-camera

(please refer to: https://github.com/IntelRealSense/realsense-ros (ros2-development branch))

Be sure to calibrate your camera and save the parameters on-board (using realsense-viewer)


## How to use me
If you installed everything you just need to do:

```
./launch.sh
```


## TODO
- Write a launch file to launch the camera and start recording (record only useful topics)
- Write the script to extract RGB and DEPTH
