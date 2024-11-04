import os
from dotenv import load_dotenv
from google.cloud import firestore

load_dotenv()

# Set up Firestore client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-file.json"
db = firestore.Client()
