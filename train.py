import cv2
import os
import numpy as np

def load_dataset(root="dataset"):
    faces, labels = [], []
    if not os.path.exists(root):
        return faces, np.array(labels, dtype=np.int32)
        
    for label in os.listdir(root):
        folder = os.path.join(root, label)
        if not os.path.isdir(folder):
            continue
        for file in os.listdir(folder):
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                path = os.path.join(folder, file)
                image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                if image is not None:
                    faces.append(image)
                    labels.append(int(label))
    return faces, np.array(labels, dtype=np.int32)

def train_model():
    print("Loading student dataset...")
    faces, labels = load_dataset("dataset")
    if len(faces) == 0:
        print("No training images found in 'dataset/' directory. Run capture.py first.")
        return

    print(f"Training LBPH Face Recognizer on {len(faces)} samples...")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, labels)

    os.makedirs("trainer", exist_ok=True)
    trainer_path = os.path.join("trainer", "trainer.yml")
    recognizer.write(trainer_path)
    print(f"Model successfully trained and saved to {trainer_path}")

if __name__ == "__main__":
    train_model()
