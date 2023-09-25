import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS product
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price FLOAT,
            picture TEXT
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO product (name, price, picture)
        VALUES ('Гарри Потер', 2000.0, 'images/nom1.jpeg'),
                ('python', 3000.0, 'images/nom2.jpeg'),
                ('48 законов жизни', 4000.0, 'images/nom3.jpeg'),
                ('Герой нашего времени', 5000.0, 'images/nom4.jpg')
        """
    )
    db.commit()


def get_products():
    cursor.execute(
        """
        SELECT * FROM product
        """
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()