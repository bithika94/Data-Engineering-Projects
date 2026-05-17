import os
import psycopg2

print("Starting connection test...")

db_host = os.getenv("DB_HOST", "localhost")
db_port = int(os.getenv("DB_PORT", "5432"))
db_name = os.getenv("DB_NAME", "products")
db_user = os.getenv("DB_USER", "postgres")
db_pass = os.getenv("DB_PASS", "postgres")

new_vegetable = ("Parsnips", "Fresh", 2.42, 2.19)

conn = None

try:
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_pass
    )

    print("Connected successfully")

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS vegetables (
            id SERIAL PRIMARY KEY,
            name TEXT,
            form TEXT,
            retail_price NUMERIC,
            cup_equivalent_price NUMERIC
        );
    """)

    cur.execute(
        """
        INSERT INTO vegetables (name, form, retail_price, cup_equivalent_price)
        VALUES (%s, %s, %s, %s);
        """,
        new_vegetable
    )

    conn.commit()

    cur.close()
    print("ETL complete. 1 row inserted.")

except Exception as e:
    print("Error during ETL:")
    print(e)

finally:
    if conn:
        conn.close()
        print("Connection closed")

print("Test completed")
