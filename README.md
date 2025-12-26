Unique Person Detection & Counting using YOLOv8
Overview

This project implements a real-time CCTV analytics system to detect, track, and count unique persons in video streams. Leveraging YOLOv8 for detection and a centroid-based multi-object tracking algorithm, the system ensures accurate counting without duplicates.

Features

Real-time person detection using YOLOv8 (YOLOv8n for lightweight inference).

Unique person counting with ID-based tracking to avoid double-counting.

Annotated video output with live person count overlay.

High real-time performance (~30 FPS) on standard hardware.

Works with CCTV or pre-recorded video streams.

Installation

Clone the repository:

git clone https://github.com/<your-username>/unique-person-detection.git
cd unique-person-detection


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt

Usage

Place your test video in the videos/ folder.

Run the detection and tracking script:

python detect_and_count.py --source videos/test_video.mp4 --weights yolov8n.pt


Output:

Annotated video saved in output/ folder.

Live person count displayed on video frames.

Experimental Results

Detected X unique persons in the test video.

0 duplicate counts across frames.

Achieved ~30 FPS processing with YOLOv8n.

Tools & Technologies

Python

OpenCV

YOLOv8 (Ultralytics)

Centroid-based Multi-Object Tracking

Computer Vision

Future Improvements

Integration with alert system for crowd detection thresholds.

Extend tracking to face recognition for better identity verification.

Optimize for edge devices for fully deployed CCTV systems.
