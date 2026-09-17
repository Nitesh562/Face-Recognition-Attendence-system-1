import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="face_attendance"
    )

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        roll_no VARCHAR(50) NOT NULL,
        class_name VARCHAR(50) NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        attendance_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT NOT NULL,
        attendance_date DATE NOT NULL,
        attendance_time TIME NOT NULL,
        status VARCHAR(20) DEFAULT 'Present',
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    ''')
    conn.commit()
    conn.close()

def add_student(student_id, name, roll_no, class_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO students (student_id, name, roll_no, class_name) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (student_id, name, roll_no, class_name))
    conn.commit()
    conn.close()

def get_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, roll_no, class_name FROM students WHERE student_id=%s", (student_id,))
    res = cursor.fetchone()
    conn.close()
    return res

def already_marked(student_id, date_value):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT attendance_id FROM attendance WHERE student_id=%s AND attendance_date=%s", (student_id, date_value))
    res = cursor.fetchone()
    conn.close()
    return res is not None

def mark_attendance(student_id):
    from datetime import datetime
    conn = get_db_connection()
    cursor = conn.cursor()
    now = datetime.now()
    if already_marked(student_id, now.date()):
        conn.close()
        return False
    cursor.execute(
        "INSERT INTO attendance (student_id, attendance_date, attendance_time, status) VALUES (%s, %s, %s, %s)",
        (student_id, now.date(), now.time(), "Present")
    )
    conn.commit()
    conn.close()
    return True
