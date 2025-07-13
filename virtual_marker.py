import cv2
import mediapipe as mp
import numpy as np

#pipeline
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
