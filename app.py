from flask import Flask, send_file, jsonify, request
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        "status": "online",
        "project": "Automatic Attendance System Using Face Recognition",
        "institution": "Dr. Shyama Prasad Mukherjee University, Ranchi"
    })

if __name__ == '__main__':
    print("-------------------------------------------------------------------")
    print("FaceTrack AI Web Application Running!")
    print("Open your browser and visit: http://127.0.0.1:5000")
    print("-------------------------------------------------------------------")
    app.run(host='0.0.0.0', port=5000, debug=True)
