from sqlalchemy import inspect
from database.db_connector import db_connector

def get_schema_metadata():
    """
    Retrieve the schema metadata dynamically from the PostgreSQL database.
    Returns:
        dict: A dictionary of tables, columns, and their data types.
    """
    engine = db_connector.connect()
    inspector = inspect(engine)
    schema = {}

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = {col['name']: str(col['type']) for col in columns}

    return schema
