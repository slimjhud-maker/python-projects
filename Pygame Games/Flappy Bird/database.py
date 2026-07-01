import sqlite3 as sql
import settings as s

connection = sql.connect(s.databasePath)
cursor = connection.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userID VARCHAR UNIQUE,
        password VARCHAR
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userID VARCHAR UNIQUE,
        score INTEGER
        )
    """)
    connection.commit()


def sign_up(userID, password):
    try:
        cursor.execute("INSERT INTO users(userID, password) VALUES(?, ?)", (userID, password))
        connection.commit()
        print("username acceptable")
    except Exception as e:
        print("username already in use")


def sign_in():
    pass
    # connection.commit()


def save_score():
    pass
    # connection.commit()




create_tables()
connection.commit()