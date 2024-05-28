import os
import psycopg2

def create_connection():
    os.environ['DB_USERNAME'] = "appFlask"
    os.environ['DB_PASSWORD'] = "abc@1234"

    conn = psycopg2.connect(
        host="localhost",
        database="barbershopdb",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    
    return conn
