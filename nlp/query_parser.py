import openai
import os
import re
from database.schema_explorer import get_schema_metadata

# Load the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_query(user_query: str):
    """
    Convert a natural language query into an SQL query using the OpenAI API.
    Args:
        user_query (str): Natural language query.
    Returns:
        str: Generated SQL query.
    """
    # Get the database schema
    schema_metadata = get_schema_metadata()
    schema_info = "\n".join([
        f"Table '{table}': {', '.join([f'{col} ({dtype})' for col, dtype in columns.items()])}"
        for table, columns in schema_metadata.items()
    ])

    # Prepare the system and user messages for the Chat API
    messages = [
        {"role": "system", "content": f"The database schema is as follows:\n{schema_info}\nConvert the following natural language query into an SQL query."},
        {"role": "user", "content": user_query}
    ]

    # Call the OpenAI Chat API
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=messages,
        max_tokens=200
    )

    # Extract the generated SQL query from the response
    sql_query = response.choices[0].message.content.strip()

    # Clean the SQL query by removing any backticks or Markdown code block markers
    cleaned_sql_query = re.sub(r"```.*?```", "", sql_query, flags=re.DOTALL).strip()
    cleaned_sql_query = cleaned_sql_query.replace("```sql", "").replace("```", "").strip()

    return cleaned_sql_query
