# This script is for updating the database schema if you need to make changes to the tables after the app is already running. 
# Like, if you want to add a new column or something. Helps keep the database up to date without losing data.

import sqlite3

DATABASE = 'database.db'

def update_schema():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Add missing columns to the users table
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN profile_picture TEXT")
    except sqlite3.OperationalError:
        print("Column 'profile_picture' already exists.")

    try:
        cursor.execute("ALTER TABLE users ADD COLUMN bio TEXT")
    except sqlite3.OperationalError:
        print("Column 'bio' already exists.")

    try:
        cursor.execute("ALTER TABLE users ADD COLUMN date_of_birth TEXT")
    except sqlite3.OperationalError:
        print("Column 'date_of_birth' already exists.")

    conn.commit()
    conn.close()
    print("Database schema updated successfully.")

if __name__ == "__main__":
    update_schema()
