# 🖊️ Virtual Marker using Hand Gestures

A Python-based virtual drawing tool that lets you draw on screen using only your **index finger** and a **webcam**.<br>
No mouse, no touchscreen — just gestures and real-time magic using **OpenCV** and **MediaPipe**.

---

## 🚀 Features

- 🖐️ Draw using index finger gestures
- 🎨 Manual color selection via keyboard
- 🧼 Clear screen with a key
- 💾 Save your drawings
- 🖥️ Real-time webcam feed + canvas overlay
- 🔥 Smooth and responsive hand tracking

---

## 🎥 Demo

https://github.com/yourusername/virtual-marker-handgestures/assets/demo.gif  
(*You can upload a GIF or link to a YouTube video demo*)

---

## 🧰 Tech Stack

- 🐍 Python 3.x
- 📷 OpenCV
- ✋ MediaPipe (for hand tracking)
- 🧮 NumPy

---

## 🖥️ How It Works

1. Uses **MediaPipe** to detect hand landmarks
2. Tracks **index finger tip** to detect drawing motion
3. When only index finger is up ➝ starts drawing
4. Combines drawing on a transparent canvas with webcam feed
5. Color selection and actions are handled with keyboard input

---

## 🎨 Controls

| Key     | Action                  |
|---------|--------------------------|
| `1`     | Select Purple color      |
| `2`     | Select Green color       |
| `3`     | Select Red color         |
| `C`     | Clear canvas             |
| `S`     | Save current drawing     |
| `Q`     | Quit the app             |
| ✋ Gesture | Index finger up to draw |

---

## 🧪 Installation

### 🔧 Requirements

Install dependencies:

```bash
pip install opencv-python mediapipe numpy
