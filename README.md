
# 🚀 Dynamic SQL Query Generator with FastAPI and LLM Integration

This project allows users to generate SQL queries dynamically from natural language inputs using a FastAPI backend and an LLM (Large Language Model) such as OpenAI's GPT-3.5 or GPT-4.

## **Table of Contents**

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## **Overview**

This application enables users to submit natural language queries, which are then converted into SQL queries using an LLM (like OpenAI's GPT). The generated SQL is executed on a PostgreSQL database, and the results are returned in a user-friendly format.

---

## **Features**

- 🌐 **FastAPI Backend**: A lightweight and fast backend framework.
- 🤖 **LLM Integration**: Convert natural language to SQL queries using OpenAI's API.
- 🛠️ **Dynamic SQL Execution**: Execute SQL queries on PostgreSQL dynamically.
- 🔍 **Error Handling**: Robust error handling for invalid queries.
- 📊 **Formatted Results**: Display query results in a readable format with line-by-line spacing.

---

## **Prerequisites**

Ensure you have the following tools installed:

- **Python** (>= 3.8)
- **PostgreSQL** (>= 12)
- **pip** (Python package manager)
- **Git** (optional)

### **API Key**

You'll need an **OpenAI API key** to use the LLM services. Get it here: [OpenAI API Keys](https://platform.openai.com/account/api-keys)

---

## **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/dynamic-sql-generator.git
   cd dynamic-sql-generator
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**

   Create a database in PostgreSQL:

   ```sql
   CREATE DATABASE dynamic_sql;
   ```

---

## **Configuration**

1. **Create a `.env` File**

   Create a `.env` file in the project root and add the following environment variables:

   ```plaintext
   POSTGRES_URI=postgresql://username:password@localhost:5432/dynamic_sql
   OPENAI_API_KEY=your_openai_api_key
   ```

2. **Update Database Connection**

   Make sure your PostgreSQL credentials are correct in the `.env` file.

---

## **Usage**

1. **Run the FastAPI Server**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Documentation**

   Open your browser and go to:

   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

3. **Make a Request**

   Use **Swagger UI** or a tool like **cURL** or **Postman** to test the endpoint.

   ### Example Request Using cURL:

   ```bash
   curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{
     "user_query": "List all products with an actual price greater than 1000, rating above 4.5, and discount percentage above 50%"
   }'
   ```

---

## **API Endpoints**

### **1. Root Endpoint**

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.

#### **Example Response**

```json
{
  "message": "Dynamic SQL Querying API is running!"
}
```

### **2. Query Endpoint**

- **URL**: `/query`
- **Method**: `POST`
- **Description**: Converts a natural language query to SQL, executes it, and returns the results.

#### **Request Body**

```json
{
  "user_query": "List all products with a price greater than 1000."
}
```

#### **Example Response**

```json
{
  "sql_query": "SELECT * FROM products WHERE price > 1000;",
  "results": [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 1500}
  ]
}
```

---

## **Troubleshooting**

1. **Database Connection Issues**:
   - Ensure PostgreSQL is running.
   - Verify the credentials in the `.env` file.

2. **OpenAI API Errors**:
   - Check your OpenAI API key.
   - Verify you have sufficient quota for API calls.

3. **Empty SQL Query**:
   - Ensure the `parse_query` function generates valid SQL. Print the output for debugging.

---


## **License**

This project is licensed under the **MIT License**.

---

## **Acknowledgments**

- **OpenAI** for the GPT models.
- **FastAPI** for the backend framework.
- **SQLAlchemy** for database integration.

---

Happy coding! 😊🚀
