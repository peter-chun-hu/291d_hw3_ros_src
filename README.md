# ROS SLAM
## Introduction
Implemented ROS launch file to build a map using ROS packages

## Environment
Real world  
<img src="img/Environment1.jpg" width="575">  
Map  
<img src="img/Environment2.JPG" width="575">  

## **Results**
* ### Image
  <img src="img/Result1.jpg" width="575">  
* ### rqt_graph
  <img src="img/rqt_graph.JPG" width="700">  
* ### Video (Click the image below to play on YouTube)
  [![](http://img.youtube.com/vi/bA_MkM1NLRY/0.jpg)](http://www.youtube.com/watch?v=bA_MkM1NLRY)
* ### [Report](report.pdf)

## **Requirements**
* ### Ubuntu 16.04
* ### ROS Kinetic

## **Installment**
* ### Put repository *SLAM_ROS/src* under ROS Workspace, i.e. ```~/catkin_ws```
* ### Put repository *SLAM_ROS/share* under ROS package path, i.e. ```/opt/ros/kinetic```

## **Run**
* ### Launch ROS launch file with ```roslaunch HW3.launch``` under ```/opt/ros/kinetic/share/usb_cam/launch```

## **ROS packages**
* ### [usb camera](http://wiki.ros.org/usb_cam)
* ### [joystick](http://wiki.ros.org/joy)
* ### [aruco](http://wiki.ros.org/tuw_aruco)
* ### [SLAM](http://wiki.ros.org/tuw_marker_slam)
