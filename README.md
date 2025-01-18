# FitTrack-AI


FitTrack-AI is an intelligent fitness tracking project that leverages OpenCV and MediaPipe to assist users in performing workouts accurately. It identifies human poses, evaluates specific body parts, and provides workout counts in real-time. This project is designed to help users monitor and improve their workout techniques efficiently.

## Project Structure

The project consists of three main components:

# 1. Ai_Trainer

The core script where the video input is processed and workout logic is implemented.

Responsibilities:

Accepts video input from a webcam or file.

Analyzes workout movements.

Tracks and counts workout repetitions based on predefined logic.

# 2. PoseModule

A specialized module that detects human poses during workouts.

Responsibilities:

Utilizes MediaPipe for pose detection.

Identifies specific body parts related to the workout.

Outputs pose landmarks for analysis.

# 3. PoseProject.py

A testing script for validating the functionality of the PoseModule.

Responsibilities:

Ensures accurate detection of poses.

Tests the integration and performance of the PoseModule.

## Features

* Real-Time Pose Detection: Detects and tracks human poses with high accuracy.

* Workout Count Logic: Implements intelligent algorithms to count workout repetitions.

* Targeted Feedback: Focuses on specific body parts for precise evaluation.

* Seamless Integration: Combines the capabilities of OpenCV and MediaPipe.

## Requirements

To run this project, you need the following:

Python 3.7 or higher

Required libraries:

- OpenCV

- MediaPipe

- NumPy

Install dependencies using:

```bash
pip install -r requirements.txt

## How to Use

Clone the repository:

git clone https://github.com/Josephvarghes/fittrack-ai
cd FitTrack-AI

Run the main script:

python Ai_Trainer.py

Use PoseProject.py to test the PoseModule:

python PoseProject.py

Input your workout video or use a webcam for real-time tracking.

```
## Workflow

Pose Detection: The PoseModule detects key landmarks of the user's body in real-time.

Workout Analysis: Ai_Trainer analyzes the detected poses to count repetitions and evaluate technique.

Feedback Generation: Provides insights and feedback for improving the workout.

## Project Demo

Add a gif or screenshots showing:

 Real-time pose detection

Workout count interface

Pose landmark visualization

## Future Enhancements

Integration of additional workouts.

Support for more body movements and exercises.

Advanced feedback with AI recommendations.

Mobile application version.