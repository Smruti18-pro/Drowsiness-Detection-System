import cv2
import time
import winsound

# Load Haar Cascade files
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# Start webcam
cap = cv2.VideoCapture(0)

eye_closed_start = None

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not detected!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_found = 0

    for (x, y, w, h) in faces:

        # Draw face rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=3
        )

        eyes_found += len(eyes)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                frame,
                (x+ex, y+ey),
                (x+ex+ew, y+ey+eh),
                (0, 255, 0),
                2
            )

    # Check if eyes are closed
    if eyes_found == 0:

        if eye_closed_start is None:
            eye_closed_start = time.time()

        elapsed = time.time() - eye_closed_start

        cv2.putText(
            frame,
            f"Eyes Closed: {int(elapsed)} sec",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        # Alarm after 2 seconds
        if elapsed >= 2:

            cv2.putText(
                frame,
                "DROWSINESS ALERT!",
                (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

            winsound.Beep(2500, 1000)

    else:
        eye_closed_start = None

    cv2.imshow("Drowsiness Detection System", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
