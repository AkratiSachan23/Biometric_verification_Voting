from flask import Flask, request, jsonify
import os
import cv2
from backend.database.db_operations import register_voter

app = Flask(__name__)

IMAGE_SAVE_PATH = "backend/images/registered_faces/"

@app.route('/register', methods=['GET','POST'])
def register():
    data = request.json
    voter_id = data.get("voter_id")

    if not voter_id:
        return jsonify({"error": "Voter ID is required"}), 400

    # Capture Image (Simulating Face Lock System)
    cam = cv2.VideoCapture(0)  # Open webcam
    ret, frame = cam.read()
    cam.release()

    if not ret:
        return jsonify({"error": "Failed to capture image"}), 500

    # Save Image
    os.makedirs(IMAGE_SAVE_PATH, exist_ok=True)
    image_path = f"{IMAGE_SAVE_PATH}{voter_id}.jpg"
    cv2.imwrite(image_path, frame)

    # Store in MongoDB
    register_voter(voter_id, image_path)

    return jsonify({"message": "Voter Registered Successfully!", "image_path": image_path}), 201

if __name__ == '__main__':
    app.run(port=5001, debug=True)
