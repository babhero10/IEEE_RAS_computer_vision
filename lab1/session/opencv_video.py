import cv2

cap = cv2.VideoCapture('videos/video.mp4')

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()


while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't receive frame.")
        break

    cv2.imshow('Camera Feed', cv2.resize(frame, (640, 480)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
