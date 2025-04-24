from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    """Create a SQLAlchemy engine for MySQL database connection."""
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    connection_str = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    return create_engine(connection_str)

def get_select_query(q):
    """Construct a SQL SELECT query based on the provided dictionary."""
    sql = "SELECT " + q["fields"]
    if q.get("table"):
        sql += " FROM " + q["table"]
    if q.get("condition"):
        sql += " WHERE " + q["condition"]
    if q.get("group"):
        sql += " GROUP BY " + q["group"]
    if q.get("group_condition"):
        sql += " HAVING " + q["group_condition"]
    if q.get("order"):
        sql += " ORDER BY" + q["order"]
    sql += ";"
    return sql

def get_result(command: str, conn):
    """Execute a SQL command and print the results."""
    result = conn.execute(text(command))
    for row in result:
        print(row)
    print()
    return result