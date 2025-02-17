from backend.database.db_connection import voters_collection, faces_collection
import face_recognition
import numpy as np

# Register a voter in the database
def register_voter(voter_id, name, image_path):
    """
    Registers a voter with their face encoding.
    """
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)

    if not encoding:
        return "Face encoding failed!"

    voter_data = {
        "voter_id": voter_id,
        "name": name,
        "face_embedding": encoding[0].tolist()  # Store as list
    }

    voters_collection.insert_one(voter_data)
    return f"Voter {name} registered successfully!"


# Fetch voter by ID
def get_voter_by_id(voter_id):
    return voters_collection.find_one({"voter_id": voter_id})

# Store face data
def save_face_data(voter_id, face_embedding):
    """
    Saves face embedding into the faces collection.
    """
    face_data = {
        "voter_id": voter_id,
        "face_embedding": face_embedding.tolist()  # Ensure it's stored as a list
    }
    faces_collection.insert_one(face_data)
    return "Face data stored successfully!"

# Fetch stored face embedding for verification
def get_face_data(voter_id):
    """
    Retrieves stored face embedding from the database and converts it to a NumPy array.
    """
    record = faces_collection.find_one({"voter_id": voter_id})
    return np.array(record["face_embedding"]) if record else None  # Convert to NumPy array
