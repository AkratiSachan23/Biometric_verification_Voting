from flask import Flask, request, jsonify
import cv2
import face_recognition
import numpy as np
from backend.database.db_operations import get_face_data  # Ensure this returns embeddings, not image paths

app = Flask(__name__)

@app.route('/verify', methods=['GET','POST'])
def verify():
    data = request.json
    voter_id = data.get("voter_id")

    if not voter_id:
        return jsonify({"error": "Voter ID is required"}), 400

    # Retrieve stored face encoding from MongoDB
    stored_encoding = get_face_data(voter_id)
    if not stored_encoding:
        return jsonify({"error": "Voter not found"}), 404

    # Convert stored encoding to NumPy array
    stored_encoding = np.array(stored_encoding)

    # Capture Live Image for Verification
    cam = cv2.VideoCapture(0)  # Open webcam
    ret, live_frame = cam.read()
    cam.release()

    if not ret:
        return jsonify({"error": "Failed to capture live image"}), 500

    # Convert BGR to RGB (face_recognition expects RGB format)
    live_frame = cv2.cvtColor(live_frame, cv2.COLOR_BGR2RGB)

    # Extract Face Encoding from Captured Image
    live_encoding = face_recognition.face_encodings(live_frame)

    if len(live_encoding) == 0:
        return jsonify({"error": "No face detected in live image"}), 400

    live_encoding = live_encoding[0]  # Extract the first face found

    # Compare Faces using Face Distance
    distance = face_recognition.face_distance([stored_encoding], live_encoding)[0]
    match = distance < 0.6  # Lower threshold means stricter match

    if match:
        return jsonify({"message": "Verification successful!", "voter_id": voter_id, "match_confidence": 1 - distance}), 200
    else:
        return jsonify({"message": "Face mismatch!", "match_confidence": 1 - distance}), 403

if __name__ == '__main__':
    app.run(port=5002, debug=True)
