import os
import psycopg2

conn = psycopg2.connect(
    database=os.environ.get('db_database'),
    host=os.environ.get('db_host'),
    user=os.environ.get('db_user'),
    password=os.environ.get('db_password'),
    port=os.environ.get('db_port'),
)

cursor = conn.cursor()
