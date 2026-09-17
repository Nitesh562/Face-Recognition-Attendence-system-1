-- MySQL Relational Schema for BCA Face Recognition Attendance System
-- Faculty: Shweta Kumari & Jaffar Abbas
-- Department of Computer Application (BCA Semesters 1 to 6)

CREATE DATABASE IF NOT EXISTS face_attendance;
USE face_attendance;

CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) DEFAULT 'BCA'
);

INSERT IGNORE INTO teachers (username, password_hash, full_name, department) VALUES
('shweta', 'admin123', 'Shweta Kumari', 'BCA'),
('jaffar', 'admin123', 'Jaffar Abbas', 'BCA');

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(50) NOT NULL,
    class_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    attendance_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Present',
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- BCA Students 1 to 10 across Semesters 1 to 6
INSERT IGNORE INTO students (student_id, name, roll_no, class_name) VALUES
(1, 'Aarav Sharma', '24BCA01', 'BCA Semester 1'),
(2, 'Ananya Patel', '24BCA02', 'BCA Semester 1'),
(3, 'Rohan Kumar', '23BCA03', 'BCA Semester 2'),
(4, 'Sneha Kumari', '23BCA04', 'BCA Semester 2'),
(5, 'Vikram Singh', '22BCA05', 'BCA Semester 3'),
(6, 'Pooja Verma', '22BCA06', 'BCA Semester 4'),
(7, 'Amit Yadav', '21BCA07', 'BCA Semester 5'),
(8, 'Neha Gupta', '21BCA08', 'BCA Semester 5'),
(9, 'Kunal Das', '20BCA09', 'BCA Semester 6'),
(10, 'Riya Sen', '20BCA10', 'BCA Semester 6');
