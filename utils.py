# This file is for helper functions used across BookRivals. 
# Stuff that doesn't fit directly in the models or routes, like utility functions for formatting dates or checking password strength, goes here. 
# Makes the code cleaner and easier to manage.

import sqlite3
from flask import request, redirect
from datetime import datetime

DATABASE = "database.db"

def get_follower_count(username):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM followers WHERE following=?", (username,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_like_count(post_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM likes WHERE post_id=?", (post_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def is_following(follower, following):
    if not follower or not following:
        return False
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM followers WHERE follower=? AND following=?",
                  (follower, following))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def is_liked(username, post_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM likes WHERE username=? AND post_id=?", (username, post_id))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def redirect_back(default='/'):
    return redirect(request.referrer or default)

def get_display_name(email):
    """Return the part of the email before the @ sign."""
    if not email:
        return ''
    return email.split('@')[0]
