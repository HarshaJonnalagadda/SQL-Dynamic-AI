import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
POSTGRES_URI = os.getenv("POSTGRES_URI")
print(f"POSTGRES_URI: {POSTGRES_URI}")
# Connect to PostgreSQL
engine = create_engine(POSTGRES_URI)

# Load the CSV dataset
df = pd.read_csv("datasets/amazon.csv")

# Inspect the columns
print(df.head())

# Import data into PostgreSQL (table name: 'amazon_sales')
df.to_sql("amazon_sales", engine, if_exists="replace", index=False)

print("Data imported successfully!")
