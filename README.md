# Drowsiness Detection and Alert System

## Project Overview

The Drowsiness Detection and Alert System is a computer vision-based application developed using Python and OpenCV. The system continuously monitors the user's face and eyes through a webcam. If the eyes remain closed for a specified period, the system identifies the user as drowsy and triggers an alarm to alert them.

This project helps improve safety by preventing accidents caused by fatigue and loss of attention.

## Features

* Real-time face detection
* Real-time eye detection
* Continuous webcam monitoring
* Drowsiness detection based on eye closure
* Audio alert system using alarm sound
* User-friendly and easy to operate

## Technologies Used

* Python
* OpenCV
* Haar Cascade Classifiers
* Winsound Module
* Computer Vision

## Hardware Requirements

* Laptop/Desktop Computer
* Webcam
* Speaker or Headphones

## Software Requirements

* Windows 10/11
* Python 3.x
* OpenCV Library

## Project Structure

Drowsiness-Detection-System/

├── Drowsiness.py

├── haarcascade_frontalface_default.xml

├── haarcascade_eye.xml

├── README.md

└── requirements.txt

## Installation

1. Install Python.
2. Install OpenCV:

pip install opencv-python

3. Download Haar Cascade XML files.
4. Place all files in the same project folder.

## How to Run

1. Open the project folder.
2. Run the Python file:

python Drowsiness.py

3. The webcam will start automatically.
4. If eyes remain closed for a few seconds, an alarm will be triggered.

## Working Principle

1. Capture live video from webcam.
2. Detect face using Haar Cascade classifier.
3. Detect eyes within the face region.
4. Monitor eye status continuously.
5. If eyes are closed for a predefined duration:

   * Display "DROWSINESS ALERT!"
   * Trigger alarm sound.
6. Continue monitoring until the user exits the program.

## Applications

* Driver Drowsiness Monitoring
* Student Attention Monitoring
* Workplace Safety Systems
* Fatigue Detection Systems
* Smart Surveillance Applications

## Advantages

* Low-cost implementation
* Real-time monitoring
* Easy to use
* Helps improve safety
* Lightweight and efficient

## Limitations

* Performance depends on lighting conditions.
* Haar Cascade may not accurately detect partially closed eyes.
* Detection accuracy decreases if the face is not clearly visible.

## Future Enhancements

* MediaPipe Face Mesh Integration
* Eye Aspect Ratio (EAR) Calculation
* Mobile Notifications
* AI-Based Drowsiness Prediction
* Cloud-Based Monitoring System

## Output

* Face Detection
* Eye Detection
* Drowsiness Alert Message
* Alarm Sound Notification

## Author

Smruti Ranjan Sahoo

## License

This project is developed for educational and academic purposes.
