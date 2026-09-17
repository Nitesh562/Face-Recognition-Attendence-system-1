import cv2
import os
from datetime import datetime
import database

def recognize_attendance():
    FACE_CASCADE = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_detector = cv2.CascadeClassifier(FACE_CASCADE)

    recognizer_path = os.path.join("trainer", "trainer.yml")
    if not os.path.exists(recognizer_path):
        print("Trainer file not found! Please run train.py first.")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(recognizer_path)
    print("LBPH Recognizer model loaded successfully.")

    cam = cv2.VideoCapture(0)
    print("Starting video feed for attendance. Press ESC to stop.")

    while True:
        ok, frame = cam.read()
        if not ok:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(80, 80))

        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            student_id, confidence = recognizer.predict(face_roi)

            # Lower confidence in LBPH means a better match (< 75 is typically recognized)
            if confidence < 75:
                student = database.get_student(student_id)
                name = student[1] if student else f"ID {student_id}"
                roll = student[2] if student else ""
                
                # Duplicate attendance check & marking
                marked = database.mark_attendance(student_id)
                status_text = "Present Marked" if marked else "Already Marked"
                color = (0, 255, 0) if marked else (0, 255, 255)

                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, f"{name} ({roll})", (x, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                cv2.putText(frame, f"{status_text} | Conf: {int(100 - confidence)}%", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, "Unknown Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Live Attendance System - Press ESC to exit", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_attendance()
