<div align="center">

# Simple YOLO Object Detection

Minimal Python implementation of real-time YOLO object detection using a camera feed.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Reference%20Implementation-6366F1)

</div>

---

## Overview

Minimal Python implementation of real-time YOLO object detection using a camera feed.

## Highlights

- Live webcam capture
- YOLOv8 object detection
- Class labels and confidence scores
- Beginner-friendly implementation

## Tech Stack

Python · Ultralytics YOLOv8 · OpenCV

## Getting Started

```bash
git clone https://github.com/haseebconventarian2-gif/simple-yolo-implementation.git
cd simple-yolo-implementation
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
```

## Configuration

Place YOLOv8 Nano weights at `yolo-Weights/yolov8n.pt` and connect a webcam.

> Store credentials in `.env` and never commit secrets.

## Run

```bash
pip install ultralytics opencv-python
python object.py
```

## Project Status

This is a learning and reference implementation. Review security, validation, monitoring, and deployment settings before production use.
