from google.cloud import vision
import cv2
import os
from backend.database.db_operations import fetch_face
import face_recognition

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/vision_api_key.json"

def detect_faces(image_path):
    """Detect faces in an image using Google Vision API."""
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations

    if len(faces) == 0:
        return None, "No face detected."
    
    return faces, "Face detected."

def compare_faces(voter_id):
    """Compare registered face with live captured face using Google Vision API."""
    registered_image_path = fetch_face(voter_id)
    if not registered_image_path:
        return False, "No registered face found."

    # Capture Live Image
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    live_image_path = f"images/live_faces/{voter_id}.jpg"
    cv2.imwrite(live_image_path, frame)
    cap.release()

    registered_encoding = face_recognition.face_encodings(face_recognition.load_image_file(registered_image_path))[0]
    live_encoding = face_recognition.face_encodings(frame)

    if not live_encoding:
        return False, "Face not detected in live image."

    live_encoding = live_encoding[0]

    # Compare using embeddings instead of bounding boxes
    match = face_recognition.compare_faces([registered_encoding], live_encoding)
    return match[0], f"Match Confidence: {match[0]}"