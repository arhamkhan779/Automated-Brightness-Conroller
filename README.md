# 📹 Automated Video Controller

[![Watch the video](https://img.youtube.com/vi/Dc999oE1myI/0.jpg)](https://youtu.be/Dc999oE1myI)

## 📜 Overview

The **Automated Video Controller** is an innovative project that uses hand tracking to dynamically control video playback and system brightness. Leveraging the power of the MediaPipe library for hand detection and OpenCV for video processing, this project enables an interactive user experience without the need for physical buttons or sliders.

## ✨ Features

- ✋ **Hand Tracking:** Real-time detection of hand landmarks using MediaPipe.
- 💡 **Brightness Control:** Adjust your system’s brightness effortlessly based on hand movements.
- 🎥 **Video Playback:** Capture and process live video from your webcam, displaying hands and brightness adjustments.
- 📊 **Interactive UI:** Visual representation of the brightness level for intuitive control.

## 📦 Installation

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/arhamkhan779/Automated-Video-Controller.git
cd Automated-Video-Controller
pip install opencv-python numpy mediapipe wmi
```

## 🚀 Usage

1. **Run the application:**

   Execute the `brightnesscontrol.py` script:

   ```bash
   python brightnesscontrol.py
   ```

2. **Control the brightness:**

   Use your hand (thumb and index finger) in front of the camera to control the brightness. The distance between your fingers will dictate the brightness level.

3. **Quit the application:**

   Press `q` to exit the program.

## 🛠️ Code Structure

- **`HandTrackingModule.py`**: Contains the `HandDetector` class for detecting and tracking hand landmarks.
- **`brightnesscontrol.py`**: The main script that integrates hand detection with brightness control functionality.
- **`LICENSE`**: License information for the project.
- **`README.md`**: Documentation for the project.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

