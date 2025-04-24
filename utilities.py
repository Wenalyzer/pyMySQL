from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    connection_str = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    return create_engine(connection_str)

def get_result(command: str, conn):
    result = conn.execute(text(command))
    for row in result:
        print(row)
    print()
    return result