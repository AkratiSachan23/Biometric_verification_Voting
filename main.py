from flask import Flask
from backend.api.voter_registration import register
from backend.api.voting_verification import verify
from backend.database.db_connection import check_connection
import os

# Initialize Flask app
app = Flask(__name__)

# Define Routes
@app.route('/register', methods=['POST'])
def register_route():
    return register()

@app.route('/verify', methods=['POST'])
def verify_route():
    return verify()

# Check MongoDB Connection and Start Server
if __name__ == "__main__":
    try:
        check_connection()
        port = int(os.getenv("PORT", 5000))
        app.run(debug=True, host="0.0.0.0", port=port)
    except Exception as e:
        print(f"Error starting server: {e}")
