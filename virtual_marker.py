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
xp, yp = 0, 0

def is_index_up(landmarks):
    tip_id = 8
    pip_id = 6
    return landmarks.landmark[tip_id].y < landmarks.landmark[pip_id].y

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lm = handLms.landmark[8]  # Index tip
            cx, cy = int(lm.x * w), int(lm.y * h)

            if is_index_up(handLms):
                cv2.circle(img, (cx, cy), 10, draw_color, cv2.FILLED)
                if xp == 0 and yp == 0:
                    xp, yp = cx, cy
                cv2.line(canvas, (xp, yp), (cx, cy), draw_color, brush_thickness)
                xp, yp = cx, cy
            else:
                xp, yp = 0, 0

    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas)

    # color button
    cv2.rectangle(img, (10, 10), (60, 60), (255, 0, 255), cv2.FILLED)
    cv2.rectangle(img, (70, 10), (120, 60), (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (130, 10), (180, 60), (0, 0, 255), cv2.FILLED)

    cv2.putText(img, "1:Purple  2:Green  3:Red", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)
    cv2.putText(img, "C:Clear  S:Save  Q:Quit", (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

    cv2.imshow("Virtual Marker", img)


    key = cv2.waitKey(1) & 0xFF
    