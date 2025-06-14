# This file has all the database models for BookRivals. It defines the User, Blog, Comment, Follower, and Like tables using SQLite. 
# Basically, it controls how all the data is stored and related in the SQLite database. Super important for how users, posts, comments, likes, and followers work!

import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash

DATABASE = "database.db"

def create_table_user():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT,
                        profile_picture TEXT,
                        bio TEXT,
                        date_of_birth TEXT)''')
    conn.commit()
    conn.close()

def add_admin_user():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    username = "admin1@gmail.com"
    password = generate_password_hash("Webrivals@123", method='pbkdf2:sha256', salt_length=8)

    cursor.execute("DELETE FROM users WHERE username = ?", ('admin',))
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (password, username))
        conn.commit()
        print("Admin user password updated successfully.")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Admin user added successfully.")

    conn.close()

def create_table_blog():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS blog (
                        id INTEGER PRIMARY KEY,
                        image TEXT,
                        title TEXT,
                        body TEXT,
                        datetime TEXT,
                        author TEXT)''')
    conn.commit()
    conn.close()

def create_table_comment():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS comment (
                        id INTEGER PRIMARY KEY,
                        post_id TEXT,
                        comment TEXT,
                        datetime TEXT,
                        author TEXT)''')
    conn.commit()
    conn.close()

def create_table_followers():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS followers (
                        follower TEXT,
                        following TEXT,
                        FOREIGN KEY(follower) REFERENCES users(username),
                        FOREIGN KEY(following) REFERENCES users(username),
                        PRIMARY KEY(follower, following)
                    )''')
    conn.commit()
    conn.close()

def create_table_likes():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS likes (
                        id INTEGER PRIMARY KEY,
                        post_id INTEGER,
                        username TEXT,
                        FOREIGN KEY (post_id) REFERENCES blog (id),
                        FOREIGN KEY (username) REFERENCES users (username))''')
    conn.commit()
    conn.close()

def fetch_all_blog_posts():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog")
    posts = cursor.fetchall()
    conn.close()
    return posts

def getPost(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog WHERE id=?", (id,))
    post = cursor.fetchone()
    conn.close()
    return post
