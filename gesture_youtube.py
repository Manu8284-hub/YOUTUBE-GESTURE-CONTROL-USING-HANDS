import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

last_action_time = 0  # Cooldown timer

def fingers_up(hand_landmarks):
    """Check which fingers are up based on landmark positions."""
    finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    finger_status = []

    for tip in finger_tips:
        y = hand_landmarks.landmark[tip].y
        finger_status.append(y < hand_landmarks.landmark[tip - 2].y)

    return finger_status

def perform_action(action):
    """Perform a keyboard action with cooldown."""
    global last_action_time
    if time.time() - last_action_time > 1:  # 1 second cooldown
        if action == "play_pause":
            pyautogui.press('space')  # Space to play/pause
            print("▶️ Play/Pause")
        elif action == "next":
            pyautogui.hotkey('shift', 'n')  # Next video
            print("⏭️ Next Video")
        elif action == "prev":
            pyautogui.hotkey('shift', 'p')  # Previous video
            print("⏮️ Previous Video")
        elif action == "vol_up":
            pyautogui.press('up')  # Volume up
            print("🔊 Volume Up")
        elif action == "vol_down":
            pyautogui.press('down')  # Volume down
            print("🔉 Volume Down")
        last_action_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame (mirror view)
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB for Mediapipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # Detect hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(handLms)

            # Gesture Mapping
            if all(fingers):  
                perform_action("play_pause")  # Open hand
            elif fingers[1] and not any(fingers[2:]):  
                perform_action("next")  # Pointing index
            elif fingers[0] and not any(fingers[1:]):  
                perform_action("vol_up")  # Thumb up
            elif not fingers[0] and fingers[4]:  
                perform_action("vol_down")  # Pinky down

    cv2.imshow("🎥 YouTube Gesture Control", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
