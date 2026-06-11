# Postgres Connection

import psycopg


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="financial_document_rag",
        user="postgres",
        password="YOUR_PASSWORD_HERE"
    )