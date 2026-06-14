import sqlite3 as sql

connection = sql.connect(r"C:\Users\raghd\OneDrive\Desktop\python_projects\Databases\SQLite\Class 3\main.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER,
        name TEXT,
        phone TEXT
    )
""")
connection.commit()


def add_data():
    id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")

    cursor.execute("INSERT INTO student(id, name, phone) VALUES (?, ?, ?)", (id, name, phone))
    connection.commit()
    print("Data successfully saved!")


def display_data():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    print("\n--- STUDENT DATA ---")
    for x in rows:
        print(x)
    print("---------------------\n")


while True:
    print("""
1. Add Data 
2. Display Data
3. Delete Data
4. Modify Data
5. Exit
""")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_data()
    if choice == 2:
        display_data()
    if choice == 5:
        break
    else:
        print("Invalid choice!")


cursor.close()
connection.close()