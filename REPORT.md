# YOLO Dataset Configuration and Meta Files Report
Name: Prasannasri  
Course: CSE (AIML)  
Topic: YOLO Dataset Configuration and Meta Files  
## Introduction

Object detection and segmentation using YOLO models require properly structured datasets and configuration files. These meta files define how the model reads images, labels, and class information.

## Dataset YAML File

The YAML file is the main configuration file in YOLO.

It contains:

* Path to dataset
* Training and validation directories
* Class names

Example:
path: dataset
train: images/train
val: images/val

names:
0: person
1: car
2: dog

This file tells the model where data is stored and what objects to detect.

## Label Files

Each image has a corresponding `.txt` file.

Format:
class_id x_center y_center width height

* class_id → object category
* coordinates → normalized (0 to 1)

These files help the model understand object positions.

## Directory Structure

A YOLO dataset is organized as:

dataset/
├── images/
│    ├── train/
│    └── val/
├── labels/
│    ├── train/
│    └── val/
└── data.yaml

Each image must have a matching label file.

## Importance of Meta Files

* Define dataset structure
* Help in training and validation
* Map class IDs to object names
* Ensure correct model predictions

## References

* Ultralytics YOLO Documentation
* https://docs.ultralytics.com
* https://docs.ultralytics.com/datasets

## Conclusion

YOLO meta files such as YAML and label files are essential for organizing datasets and enabling accurate object detection and segmentation.
