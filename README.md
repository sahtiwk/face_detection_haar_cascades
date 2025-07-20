# Simple Face Detector with OpenCV 📸

## Project Description

This is a beginner-friendly computer vision project that uses Python and OpenCV to perform basic face detection. The script loads a static image and implements the classic **Haar Cascade algorithm** to identify and draw boxes around human faces.

While Haar Cascades are fast and provide a great introduction to object detection, they have known limitations. They can be prone to noise and struggle with variations in lighting or face orientation, which sometimes leads to imperfect detections.

This project serves as a foundational step. Future updates will explore more modern and robust deep learning models to achieve higher accuracy and more reliable performance.

***

## Features

- Detects faces in a user-provided image (`input_image.jpeg`).
- Draws a green rectangle around each detected face.
- Prints the total number of faces found to the console.

***

## Requirements

You will need the following Python libraries installed:
- `opencv-python`
- `numpy`

You can install them with a single command:
```bash
pip install opencv-python numpy
