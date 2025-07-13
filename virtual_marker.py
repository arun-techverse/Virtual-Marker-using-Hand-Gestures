import cv2
import mediapipe as mp
import numpy as np

#pipeline
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Webcam & canvas setup
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
h, w, _ = frame.shape
canvas = np.zeros((h, w, 3), dtype=np.uint8)

#color
draw_color = (255, 0, 255)  # Default Purple
brush_thickness = 7
