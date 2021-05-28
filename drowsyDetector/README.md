# Drowsiness Detection
Throughout history, road accidents have always been a major contribution in the compilation of deaths and several injuries due to many factors. One of the leading factor is due to the feeling of drowsiness and/or the lack of sleep from the driver. In order to prevent such accident from occuring in the near future, many solutions come into play such as having proper rest before driving; drinking coffee to get that caffeine boost; similarly drinking any sugar heavy and energy intensive drinks; have another relative/friend to drive it for you and many more. However as this is based off of computer vision project, the proper approach to take care of our drivers, feeling all drowsy and weak, would be to have a drowsy detector system implemented in real-time.

Essentially this system will utilise feature points (landmarks) on a driver's face to determine whether the state of the eye is at an open/mid/close state. Due to the constraints and scope of this project, the only events capable of execution are to detect the drowsiness of the driver and alert it back to the driver in a flashing way.

# Project Scope
- Capture video and colour conversion from webcam.
- Detecting drowsiness from extracting key facial landmarks.

# Functional Requirements


# Technical Requirements
- Python 3.8.5
- OpenCV-python 4.5.2.52
- Dlib 19.22.0
- Imutils 0.5.4
- Numpy 1.20.3

# System Architecture
![System Architecture](drowsy-sys-arch.png)

# Testing
The following describes the hardware that have been fully tested and developed on.
- OS: Ubuntu Debian Linux 64-bit 20.04.2 LTS
- Memory: 8GB
- Processor: Intel® Core™ i5-5300U CPU
- Graphics: Mesa Intel® HD Graphics 5500
- Camera: In-built

### Future testing:
Hoping to be tested on a Raspberry Pi 3/4 with the Camera module and some other buzzer noises attached to the board.

# Result