# Insert/Query Transcation Rows

from backend.database.db_connection import get_connection


def insert_transactions(df, source_file: str):
    insert_sql = """
        INSERT INTO transactions (
            transaction_date,
            description,
            amount,
            category,
            source_file
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    records = [
        (
            row["date"],
            row["description"],
            row["amount"],
            row["category"],
            source_file,
        )
        for _, row in df.iterrows()
    ]

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(insert_sql, records)

    print(f"Inserted {len(records)} transactions.")

