🎥 YouTube Gesture Control

Control YouTube videos hands-free using simple hand gestures detected by your webcam!
This project uses Computer Vision and Hand Landmark Detection to recognize gestures and trigger YouTube keyboard shortcuts.

🚀 Features

✅ Play / Pause videos with an open hand gesture
✅ Skip to next or previous video
✅ Control volume with thumbs up / pinky gestures
✅ Works in real-time using your webcam
✅ 100% touch-free YouTube navigation

🛠️ Tech Stack

Python – Main programming language

OpenCV – Webcam access & video processing

MediaPipe Hands – Detects 21 hand landmarks

PyAutoGUI – Simulates keyboard shortcuts

YouTube Keyboard Shortcuts – To control playback

🔧 How It Works

OpenCV captures frames from your webcam.

MediaPipe Hands detects and tracks 21 hand keypoints in real-time.

Gesture logic checks finger positions (thumbs up, pointing, etc.).

PyAutoGUI simulates keypresses:

Space → Play/Pause

Shift + N → Next video

Shift + P → Previous video

Arrow Up / Down → Volume control

🎮 Gesture Mapping
Gesture	Action
👋 Open hand	Play / Pause
👉 Pointing	Next Video
👍 Thumb up	Volume Up
👇 Pinky down	Volume Down
🖥️ Installation & Setup
# Clone the repo
git clone https://github.com/your-username/youtube-gesture-control.git
cd youtube-gesture-control

# Install dependencies
pip install opencv-python mediapipe pyautogui


Run the script:

python gesture_youtube.py

📹 How to Use

Open YouTube in your browser.

Run gesture_youtube.py.

Show gestures in front of your webcam.

Enjoy hands-free YouTube control!
