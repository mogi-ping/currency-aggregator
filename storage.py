import sqlite3


DB_NAME = "currency_data.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL NOT NULL,
            currency_pair TEXT NOT NULL,
            average_rate REAL NOT NULL,
            std_dev REAL NOT NULL,
            source TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_rate(data: dict):
    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO rates (
            timestamp,
            currency_pair,
            average_rate,
            std_dev,
            source
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            data["timestamp"],
            data["currency_pair"],
            data["average_rate"],
            data["std_dev"],
            data["source"]
        )
    )

    conn.commit()
    conn.close()