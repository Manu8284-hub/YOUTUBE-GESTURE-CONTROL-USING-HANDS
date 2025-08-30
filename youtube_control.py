import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

last_action_time = 0  # For cooldown

def fingers_up(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    finger_fold_status = []

    for tip in finger_tips:
        y = hand_landmarks.landmark[tip].y
        finger_fold_status.append(y < hand_landmarks.landmark[tip - 2].y)

    return finger_fold_status

def perform_action(action):
    global last_action_time
    if time.time() - last_action_time > 1:  # 1 second cooldown
        if action == "play_pause":
            pyautogui.press('space')
        elif action == "next":
            pyautogui.hotkey('shift', 'n')
        elif action == "prev":
            pyautogui.hotkey('shift', 'p')
        elif action == "vol_up":
            pyautogui.press('up')
        elif action == "vol_down":
            pyautogui.press('down')
        last_action_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(handLms)

            # Simple Gesture Mapping
            if all(fingers):  
                perform_action("play_pause")  # Open hand
            elif fingers[1] and not any(fingers[2:]):  
                perform_action("next")  # Point right
            elif fingers[0] and not any(fingers[1:]):  
                perform_action("vol_up")  # Thumb up
            elif not fingers[0] and fingers[4]:  
                perform_action("vol_down")  # Pinky down

    cv2.imshow("YouTube Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
