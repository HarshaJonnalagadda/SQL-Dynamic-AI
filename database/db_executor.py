from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from database.db_connector import db_connector
import re
from fastapi import HTTPException

def clean_query(sql_query: str, schema_metadata: dict) -> str:
    """
    Dynamically clean the SQL query by detecting and cleaning columns with potential formatting issues.

    Args:
        sql_query (str): The original SQL query.
        schema_metadata (dict): Database schema metadata for the relevant tables.

    Returns:
        str: The cleaned SQL query.
    """
    # Define a list of keywords for columns that may need cleaning
    potential_columns = ['price', 'amount', 'cost', 'value', 'rate', 'fee', 'rating', 'discount_percentage']

    # Find table and column names from the schema
    for table, columns in schema_metadata.items():
        for col in columns:
            # Check if the column name contains any of the potential keywords
            if any(keyword in col.lower() for keyword in potential_columns):
                # Create a cleaned version of the column to remove non-numeric characters and cast to FLOAT
                cleaned_col = f"NULLIF(REGEXP_REPLACE({col}, '[^0-9.]', '', 'g'), '')::FLOAT"
                # Replace occurrences of the column name in the query with the cleaned version
                sql_query = re.sub(rf'\b{re.escape(col)}\b', cleaned_col, sql_query)

    return sql_query

def execute_sql_query(sql_query: str, schema_metadata: dict) -> list:
    """
    Execute a given SQL query and return results.

    Args:
        sql_query (str): SQL query string.
        schema_metadata (dict): Database schema metadata for dynamic cleaning.

    Returns:
        list: Query results as a list of dictionaries.
    """
    engine = db_connector.connect()

    try:
        with engine.connect() as connection:
            # Clean the SQL query dynamically
            cleaned_sql_query = clean_query(sql_query, schema_metadata)
            print(f"Executing cleaned SQL query:\n{cleaned_sql_query}")

            # Execute the cleaned SQL query
            result = connection.execute(text(cleaned_sql_query))

            # Fetch all rows and convert to a list of dictionaries
            rows = result.fetchall()
            if rows:
                return [dict(zip(result.keys(), row)) for row in rows]
            else:
                return []
    except SQLAlchemyError as e:
        # Handle database errors gracefully and provide meaningful error messages
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        # Handle any other exceptions
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
