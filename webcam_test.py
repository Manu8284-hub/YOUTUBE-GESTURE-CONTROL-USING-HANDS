import cv2

# Open the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture frame
    if not ret:
        break

    cv2.imshow("Webcam Test", frame)  # Show video

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
