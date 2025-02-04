# ROS2 Packages for real-time Polyp and Lesion Detection for Endoscopic Procedures

## Usage

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
