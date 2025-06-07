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

## License

MIT License

Copyright (c) 2025 Prabesh Pathak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

