import cv2
import os
import database

def capture_dataset():
    FACE_CASCADE = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_detector = cv2.CascadeClassifier(FACE_CASCADE)

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    roll_no = input("Enter Roll No: ").strip()
    class_name = input("Enter Class/Semester: ").strip()

    try:
        database.add_student(int(student_id), name, roll_no, class_name)
        print(f"Student {name} registered in database.")
    except Exception as e:
        print(f"Database insertion notice: {e}")

    folder = os.path.join("dataset", student_id)
    os.makedirs(folder, exist_ok=True)

    cam = cv2.VideoCapture(0)
    count = 0
    print("Capturing 20 face samples. Please look at the camera...")

    while True:
        ok, frame = cam.read()
        if not ok:
            print("Failed to read camera frame.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(80, 80))

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            cv2.imwrite(os.path.join(folder, f"{student_id}_{count}.jpg"), face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Sample: {count}/20", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Capturing Face Samples - Press ESC to exit", frame)
        if cv2.waitKey(100) & 0xFF == 27 or count >= 20:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"Successfully saved {count} face samples in {folder}")

if __name__ == "__main__":
    capture_dataset()
