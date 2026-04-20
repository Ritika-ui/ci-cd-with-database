from app.config.config import Config
import psycopg2

def get_connection():
    return psycopg2.connect(Config.DATABASE_URL, sslmode="require")
