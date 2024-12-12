import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.engine = None

    def connect(self):
        db_uri = os.getenv("POSTGRES_URI")
        self.engine = create_engine(db_uri)
        return self.engine

db_connector = DatabaseConnector()
