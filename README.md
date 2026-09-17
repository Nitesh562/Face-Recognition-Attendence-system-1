# Automatic Attendance System Using Face Recognition
**B.Sc. Computer Application (BCA) Project**  
**Department of Computer Application, Dr. Shyama Prasad Mukherjee University, Ranchi**  
*Submitted By:* Nitesh Kumar Mahto (Roll No: 23B51185, Reg: DSPMU2023U51015)  
*Guide:* Mrs. Shweta Kumari (Assistant Professor)

---

## Project Overview
This project automates academic attendance recording using computer vision (Haar Cascade & LBPH). It eliminates proxy attendances, speeds up classroom administration, and provides digital searchable records with duplicate prevention.

## Included Files
- `index.html`: Complete interactive web application (Live webcam scanner, student registration, teacher analytics dashboard, student portal, project documentation, and 12 viva Q&A).
- `capture.py`: Captures student face samples via webcam and saves grayscale images to `dataset/{student_id}/`.
- `train.py`: Trains the LBPH Face Recognizer and exports weights to `trainer/trainer.yml`.
- `recognize.py`: Real-time face detection, recognition, duplicate checking, and attendance recording.
- `database.py`: MySQL database connection and helper methods.
- `schema.sql`: MySQL table schemas for `students` and `attendance`.
- `attendance.csv`: Exported attendance logs.

## Quick Start
1. **To run the Web Portal:**
   Double click `index.html` to open it in Google Chrome, Edge, or Firefox. Click "Start Webcam" for live scanning or "Simulate Match" for instant verification.

2. **To run the Python OpenCV System:**
   ```bash
   pip install opencv-python opencv-contrib-python mysql-connector-python numpy
   # Setup database
   mysql -u root -p < schema.sql
   # Step 1: Capture dataset
   python capture.py
   # Step 2: Train LBPH model
   python train.py
   # Step 3: Start attendance
   python recognize.py
   ```
