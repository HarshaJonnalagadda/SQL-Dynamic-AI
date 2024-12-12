from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nlp.query_parser import parse_query
from database.db_executor import execute_sql_query
from database.schema_explorer import get_schema_metadata

app = FastAPI()

# Define a Pydantic model for the request body
class QueryRequest(BaseModel):
    user_query: str

@app.get("/")
def root():
    return {"message": "Dynamic SQL Querying API is running!"}

@app.post("/query")
def query_database(request: QueryRequest):
    """
    Process a natural language query and return SQL results.
    Args:
        request (QueryRequest): Pydantic model containing the user_query.
    Returns:
        dict: Generated SQL query and results.
    """
    try:
        # Extract user_query from the request body
        user_query = request.user_query
        
        # Parse natural language query into SQL
        sql_query = parse_query(user_query)
        
        # Get the database schema metadata
        schema_metadata = get_schema_metadata()
        
        # Execute the SQL query with dynamic cleaning
        results = execute_sql_query(sql_query, schema_metadata)
        
        return {"sql_query": sql_query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
