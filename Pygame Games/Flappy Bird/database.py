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
        connection.commit()
        return True
    except sql.IntegrityError as e:
        print("username already in use")
        return False
    


def sign_in(userID, password):
    cursor.execute("SELECT userID FROM users WHERE userID = ? AND password = ?", (userID, password))
    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        return None
    


def save_score():
    pass
    # connection.commit()




create_tables()
connection.commit()