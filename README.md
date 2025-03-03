# ROS2 Packages for real-time Polyp and Lesion Detection for Endoscopic Procedures

## Dependencies
- ROS2 Jazzy Jalisco (Ubuntu 24.04)
- OpenCV

## Usage

First, clone the repository 
```bash
git clone https://github.com/akannan05/endoscope-camera.git
```
Source your ROS2 installation with:

```bash
source /opt/ros/jazzy/setup.bash
```
Then, source the current workspace installation:

```bash
cd endo_ws
source install/setup.bash
```
From here you can build all packages using
```bash
colcon build
```
That concludes the general installation for this endoscope camera package! To only build certain packages run colcon build with the `--packages-list`{:.bash} option. E.g:
```bash
colcon build --packages-list endofeed
```

## TODO (robotics software):
- [x] write publisher for endoscopic camera to endocam/feed topic
- [ ] write subscriber for inference pipeline to endocam/feed topic  
- [ ] write publisher for inferred and detected images to endocam/results topic
- [ ] write publisher for bbox coordinates to endocam/results-coords topic

## TODO (computer vision, deep learning, imaging):
- [ ] write proof of concept polyp detection model into a real-time inference pipeline
- [ ] expand classes for polyp detector (lesions and other medical landmarks)
- [ ] experiment with deformable models for enhanced imaging
- [ ] narrow band imaging script

NOTE: This repository must only contain all publisher/subscribers, services, clients, and
actions that are completely contained on the host PC. 
