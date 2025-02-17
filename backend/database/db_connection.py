import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Explicitly load the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "mongo_url.env")
load_dotenv(dotenv_path)

# Get MongoDB URI
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set!")

# Establish connection
client = MongoClient(MONGO_URI)

# Select Database (Change "voting_system" to your actual database name)
db = client["voting_system"]

# Collections (Create references for easy access)
voters_collection = db["voters"]  # Collection to store voter details
faces_collection = db["faces"]  # Collection to store face embeddings

# Function to check the connection
def check_connection():
    try:
        client.server_info()  # Will raise an exception if connection fails
        print("MongoDB Connected Successfully!")
    except Exception as e:
        print(f"MongoDB Connection Failed: {e}")

# Run connection check
if __name__ == "__main__":
    check_connection()