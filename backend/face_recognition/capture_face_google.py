import os
import cv2
from google.cloud import vision
from google.cloud import storage
from backend.database.db_operations import store_face

# Set up Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/vision_api_key.json"

IMAGE_DIR = "images/registered_faces/"

def capture_face(voter_id):
    """Capture face using OpenCV and store it locally."""
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        filename = f"{IMAGE_DIR}{voter_id}.jpg"
        cv2.imwrite(filename, frame)
        cap.release()
        cv2.destroyAllWindows()
        store_face(voter_id, filename)
        return filename

def upload_to_gcs(file_path, bucket_name="voting-images"):
    """Upload the captured image to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(os.path.basename(file_path))
    blob.upload_from_filename(file_path)
    return blob.public_url
