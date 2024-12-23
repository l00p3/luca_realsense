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

IMPORTANT: be sure to calibrate your camera and save the parameters on-board or somewhere else.
In the latter case you will not have useful information in the camera_info topic of the recorded bag.

If you want to use ROS2 camera calib refer to this link:
https://docs.nav2.org/tutorials/docs/camera_calibration.html
or read the next section.

If you want to use the software Intel RealSense D400 Series Dynamic Calibration Tool refer to this link:
https://www.intel.com/content/www/us/en/download/645988/intel-realsense-d400-series-dynamic-calibration-tool.html
On Ubuntu you need to install the software following the instruction in the link above and then run the executable "Inter.RealSense.DynamicCalibrator" installed at "/usr/bin/".


## Calibrate with ROS2 Camera Calibrator
If you decide to use the ROS2 camera calibrator node first install it:

```
sudo apt install ros-humble-camera-calibration
sudo apt install ros-humble-camera-calibration-parsers
sudo apt install ros-humble-camera-info-manager
sudo apt install ros-humble-launch-testing-ament-cmake
```

and install image pipeline package:

```
sudo apt install ros-humble-image-pipeline
```

Then, you can use the launch file:

```
ros2 launch launch/calibrate.launch.py
```

(set the correct chessboard dimension there: #squares and squares dimension).
We set the parameters in such a way it works with a A4 printed version of this chessboard:
https://github.com/opencv/opencv/blob/4.x/doc/pattern.png

(also the onw that you find in the IPB lab in A4 format).

After the calibration the parameter will be saved into "/tmp/calibrationdata.tar.gz", extract them with:

```
tar -xvf calibrationdata.tar.gz
```

### How to save the computed parameters on the camera
If you want to save the computed parameters on the camera to be published on the camera info topic follow these instructions.

First, get the serial number of your camera. This can be done by launching the camera node:

```
ros2 launch realsense2_camera rs_launch.py
```

and then copying the number that appears as a INFO message. For example:

```
[realsense2_camera_node-1] [INFO] [1733481265.392948901] [camera.camera]: Device Serial No: 215226255564
```

Then, copy the xml file from inside the camera by running the following command:

```
/usr/bin/Intel.Realsense.CustomRW -sn 215226255564 -r -f realsense_camera_215226255564.xml 
```

using the correct serial number. Them you can open the file ("realsense_camera_215226255564.xml" in this case) with your editor and modify the camera parameters. In particular, you want to modify these fields:

```
<param name = "ResolutionRGB">
        <value>1280</value>
        <value>800</value>
    </param>
    <param name = "FocalLengthRGB">
        <value>641.023</value>
        <value>640.43</value>
    </param>
    <param name = "PrincipalPointRGB">
        <value>652.651</value>
        <value>405.144</value>
    </param>
    <param name = "DistortionRGB">
        <value>-0.058282</value>
        <value>0.0700606</value>
        <value>-0.000564562</value>
        <value>0.000530918</value>
        <value>-0.0231781</value>
    </param>
```

Once this is done, you can upload the modified file onto the camera:

```
/usr/bin/Intel.Realsense.CustomRW -sn 215226255564 -w -f realsense_camera_215226255564.xml 
```

Now, you will see the new configuration published on the camera info topic (rgb topic) when you run the camera node.


## How to use me
There is some dependency that you need to install in order to launch the recording:

```
pip install pyside2 pyqt5
```

If you installed everything you just need to start the recording with:

```
ros2 launch launch/record_bag.launch.py output_folder:="/path/where/you/want/your/bag/to/be/saved/"
```

and press CTRL-C when you are done.

Then, you can use this command to extract the images:

```
python3 extract_images.py /path/of/the/bag/folder/ /path/where/you/want/your/images/
```
