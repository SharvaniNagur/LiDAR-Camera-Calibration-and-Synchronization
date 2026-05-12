# 🚗 LiDAR–Camera Calibration and Temporal Synchronization Using Target-Based Method

## 📌 Overview

This project presents a comprehensive framework for LiDAR–Camera Calibration and Temporal Synchronization using a target-based approach for autonomous vehicle perception systems.

The framework performs:

- Intrinsic camera calibration
- Extrinsic LiDAR–camera calibration
- Timestamp generation
- Temporal synchronization
- LiDAR point cloud projection onto camera frames
- Multi-sensor alignment validation

The system uses:
- Monocular Camera
- Velodyne VLP-16 LiDAR
- Checkerboard target
- MATLAB LiDAR and Computer Vision Toolboxes

The proposed methodology enables accurate spatial and temporal alignment between heterogeneous sensor systems for multi-sensor fusion applications in autonomous vehicles.

---

# 🎯 Problem Statement

Autonomous vehicles rely on multiple sensors for environmental perception and decision-making. Cameras provide rich visual information, while LiDAR sensors provide accurate 3D spatial depth information.

However, integrating these sensors introduces two major challenges:

- Spatial misalignment between LiDAR and camera coordinate systems
- Temporal mismatch due to different sensor frame rates and clock drift

This project proposes a complete calibration and synchronization pipeline to solve these issues using:
- Target-based calibration
- Timestamp synchronization
- Nearest Neighbor Matching
- LiDAR point projection

---

# 🚀 Objectives

- Perform intrinsic camera calibration
- Perform extrinsic LiDAR–camera calibration
- Generate timestamps for camera and LiDAR frames
- Synchronize heterogeneous sensor streams
- Handle clock drift between sensors
- Project LiDAR point clouds onto camera images
- Validate calibration and synchronization accuracy

---

# 🛰️ Sensors Used

## 📷 Camera

The camera captures:
- RGB image frames
- Video data
- Scene texture and visual information

### Specifications
- Frame rate: 20 FPS
- Data formats:
  - `.jpg`
  - `.mp4`

---

## 🌐 Velodyne VLP-16 LiDAR

The Velodyne VLP-16 LiDAR captures:
- 3D point cloud data
- Spatial depth information
- Environmental geometry

### Specifications
- 16-channel LiDAR
- Operating frequency: 10 Hz
- Data format:
  - `.pcap`
  - `.pcd`

---

# 🎯 Checkerboard Calibration Target

A checkerboard target is used for calibration.

### Checkerboard Specifications
- Size: 7 × 6
- Square size: 97 mm

The checkerboard helps estimate:
- Camera intrinsic parameters
- Rotation matrix
- Translation vector

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| MATLAB | Calibration and Projection |
| OpenCV | Image Processing |
| Open3D | Point Cloud Processing |
| NumPy | Numerical Computation |
| Matplotlib | Visualization |
| Velodyne VLP-16 | LiDAR Sensor |
| Wireshark | Packet Capture |
| VeloView | Point Cloud Conversion |

---

# 🔄 Complete Workflow

The proposed pipeline consists of:

1. Data Acquisition
2. Frame Extraction
3. Timestamp Generation
4. Temporal Synchronization
5. Intrinsic Calibration
6. Extrinsic Calibration
7. LiDAR–Camera Projection
8. Validation and Visualization

---

# 📥 Data Acquisition

The dataset was collected using:
- Monocular Camera
- Velodyne VLP-16 LiDAR

The camera captures:
- Images
- Video frames

The LiDAR captures:
- Raw point cloud packets in `.pcap` format

These packets are converted into:
- `.pcd` files using VeloView

---

# 🎞️ Frame Extraction

Video frames are extracted from the camera video at a predefined frame rate.

### Purpose
- Uniform frame extraction
- Consistent timestamp generation
- Synchronization preparation

### Formula

```math
F_v = \frac{fps}{desired\ frame}
```

Where:
- `fps` = frames per second
- `desired frame` = required extraction rate

---

# ⏱️ Timestamp Generation

Each frame is assigned a timestamp based on:
- Frame index
- Sensor frame rate

### Timestamp Formula

```math
T_n = \frac{n}{fps}
```

Where:
- `T_n` = timestamp of nth frame
- `n` = frame index
- `fps` = frame rate

---

# ⌛ Clock Drift Compensation

Clock drift occurs when:
- Camera and LiDAR start recording at different times

To solve this:
- Offset correction is applied during timestamp generation

### Offset Equation

```math
T_{new} = T_{original} + offset
```

This ensures accurate temporal alignment between sensors.

---

# 🔄 Temporal Synchronization

The camera and LiDAR operate at different frame rates:
- Camera → 20 FPS
- LiDAR → 10 Hz

To synchronize them:
- Nearest Neighbor Matching (NNM) is used

---

# 🎯 Nearest Neighbor Matching (NNM)

For each camera frame:
- The closest LiDAR timestamp is selected

### Synchronization Equation

```math
T_n^l = argmin |T_n^c - T_j^l|
```

Where:
- `T_n^c` = camera timestamp
- `T_j^l` = LiDAR timestamp
- `T_n^l` = nearest LiDAR frame

### Advantages
- Reduced temporal mismatch
- Improved synchronization accuracy
- Better sensor fusion

---

# 📷 Intrinsic Calibration

Intrinsic calibration determines:
- Camera focal length
- Optical center
- Lens distortion

The MATLAB Camera Calibrator App is used with checkerboard images.

---

# 📐 Intrinsic Matrix

```math
I =
\begin{bmatrix}
f_x & 0 & c_x \\
0 & f_y & c_y \\
0 & 0 & 1
\end{bmatrix}
```

Where:
- `f_x`, `f_y` = focal lengths
- `c_x`, `c_y` = optical center coordinates

---

# 🔍 Distortion Coefficients

The distortion vector includes:
- Radial distortion
- Tangential distortion

```math
dist\ coeff = [r_1 \ r_2 \ t_1 \ t_2]
```

---

# 🌐 Extrinsic Calibration

Extrinsic calibration estimates:
- Relative orientation
- Relative position

between:
- LiDAR coordinate system
- Camera coordinate system

---

# 🔄 Rotation Matrix

```math
R =
\begin{bmatrix}
r_{11} & r_{12} & r_{13} \\
r_{21} & r_{22} & r_{23} \\
r_{31} & r_{32} & r_{33}
\end{bmatrix}
```

---

# 📍 Translation Vector

```math
T = [T_1 \ T_2 \ T_3]
```

---

# 🎯 LiDAR–Camera Projection

The calibrated LiDAR points are projected onto the 2D camera image plane.

This enables:
- Visual alignment validation
- Sensor fusion
- Projection accuracy analysis

---

# 🔄 Coordinate Transformation

LiDAR points are transformed into camera coordinates.

```math
\begin{bmatrix}
X_C \\
Y_C \\
Z_C
\end{bmatrix}
=
R
\begin{bmatrix}
X_L \\
Y_L \\
Z_L
\end{bmatrix}
+ T
```

---

# 🖼️ 2D Projection

The transformed 3D points are projected onto the 2D image plane.

```math
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix}
=
K
\begin{bmatrix}
X_C/Z_C \\
Y_C/Z_C \\
1
\end{bmatrix}
```

Where:
- `(u,v)` are image pixel coordinates

---

# 🏗️ Project Architecture

## Pipeline

1. Sensor Data Input
2. Frame Extraction
3. Timestamping
4. Synchronization
5. Calibration
6. LiDAR Projection
7. Visualization

---

# 📁 Folder Structure

```text
LiDAR-Camera-Calibration-and-Synchronization/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── assets/
│   ├── setup.png
│   ├── pipeline.png
│   ├── checkerboard_detection.png
│   ├── lidar_projection.png
│   └── synchronization_output.png
│
├── src/
│   ├── frame_extraction.py
│   ├── timestamping.py
│   ├── synchronization.py
│   ├── intrinsic_calibration.py
│   ├── extrinsic_calibration.py
│   ├── lidar_projection.py
│   └── visualization.py
│
├── dataset/
│
├── results/
│   ├── projected_outputs/
│   └── calibration_results/
│
├── paper/
│   └── research_paper.pdf
│
└── matlab/
    └── calibration_scripts.m
```

---

# 📄 File Descriptions

## frame_extraction.py
Extracts video frames from camera recordings.

---

## timestamping.py
Generates timestamps for:
- Camera frames
- LiDAR point clouds

---

## synchronization.py
Implements:
- Nearest Neighbor Matching
- Temporal alignment

---

## intrinsic_calibration.py
Performs:
- Camera intrinsic calibration
- Distortion estimation

---

## extrinsic_calibration.py
Calculates:
- Rotation matrix
- Translation vector

---

## lidar_projection.py
Projects LiDAR points onto camera frames.

---

## visualization.py
Displays:
- Projected outputs
- Calibration results
- Synchronization results

---

# 📊 Experimental Results

The proposed framework successfully achieved:
- Spatial alignment
- Temporal synchronization
- Accurate LiDAR projection

The projected LiDAR points aligned correctly with camera images, validating the calibration accuracy.

---

# ✅ Advantages of Proposed Framework

- Accurate multi-sensor alignment
- Robust calibration pipeline
- Temporal synchronization handling
- Clock drift correction
- Real-time applicability
- Scalable architecture

---

# 🚗 Applications

This framework can be used in:
- Autonomous Vehicles
- ADAS Systems
- Robotics
- SLAM
- Sensor Fusion
- Environmental Perception
- Intelligent Transportation Systems

---

# 🔮 Future Scope

Possible future improvements:
- Real-time calibration
- Hardware-level synchronization
- ROS integration
- Deep learning-based calibration
- Multi-camera synchronization
- Real-time deployment on embedded systems

---


# 🏷️ GitHub Topics

Add these repository topics:
- lidar
- camera-calibration
- sensor-fusion
- autonomous-driving
- lidar-camera-calibration
- synchronization
- point-cloud
- computer-vision
- robotics
- perception



---

# 📜 License

This project is licensed under the MIT License.
