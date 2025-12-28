import cv2

# Create video capture object FIRST
cap = cv2.VideoCapture(0)

# Set width and height
cap.set(3, 640)   # width
cap.set(4, 480)   # height

while True:
    success, frame = cap.read()
    if not success:
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
