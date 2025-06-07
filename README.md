# Hand Tracking with OpenCV and Mediapipe

This project demonstrates real-time hand tracking using [OpenCV](https://opencv.org/) and [Mediapipe](https://mediapipe.dev/) in Python. It detects hand landmarks from your webcam feed and can be easily extended for gesture-based applications (e.g., controlling a snake game with your finger).

## Features

- Real-time hand detection and landmark tracking
- Configurable camera index and number of hands
- Option to select and use specific landmarks (e.g., index finger tip)
- FPS display on video feed
- Modular code with resource management

## Requirements

- Python 3.7+
- opencv-python
- mediapipe

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Usage

Run the main script:

```sh
python HandTrackingModule.py
```

- Press `q` to quit the video window.
- The script prints the position of the index finger tip (landmark 8) in the console.

## Customization

- To use a different camera, change `camera_index` in `main()` or the class constructor.
- To track different landmarks, modify the `landmark_ids` parameter in `findPosition`.

## File Structure

- `HandTracking.py` – Simple script for hand tracking.
- `HandTrackingModule.py` – Modular, class-based version with more features.
- `requirements.txt` – Python dependencies.
- `.gitignore` – Files and folders to ignore in git.



