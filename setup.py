# This script is used to set up the database with example data for BookRivals. 
# It creates some users, posts, comments, and makes sure there's always an admin user. Super useful for testing and demoing the app without having to add everything manually!
import sqlite3
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

DATABASE = 'database.db'

def seed_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Insert sample users
    users = [
        ('alice@example.com', 'Password@123', 'Passionate about technology and always eager to learn new things.'),
        ('bob@example.com', 'Secure@456', 'Nature lover, weekend traveler, and amateur photographer.'),
        ('charlie@example.com', 'Strong@789', 'Enjoys cooking, gaming, and spending time with friends.'),
        ('diana@example.com', 'Diana@321', 'Fitness enthusiast and coffee addict. Living life one day at a time.'),
        ('edward@example.com', 'Edward@654', 'Creative thinker with a love for art and design.'),
        ('fiona@example.com', 'Fiona@987', 'Music is my escape. Guitar player and concert goer.'),
        ('george@example.com', 'George@147', 'Problem solver, team player, and lifelong learner.'),
        ('hannah@example.com', 'Hannah@258', 'Dog parent, foodie, and aspiring world explorer.'),
        ('ian@example.com', 'Ian@369', 'Always up for a challenge and new experiences.'),
        ('julia@example.com', 'Julia@159', 'Optimist at heart, with a knack for making people smile.')
    ]

    # Hash passwords before inserting
    users = [(username, generate_password_hash(password, method='pbkdf2:sha256', salt_length=8), bio) for username, password, bio in users]
    cursor.executemany("INSERT OR IGNORE INTO users (username, password, bio) VALUES (?, ?, ?)", users)

    # Insert sample blog posts
    now = datetime.now()
    blogs = [
        ('media/sample1.jpg', 'Cute dog with hat', 'Exploring the forest trails during spring.', now.strftime("%d/%m/%Y, %H:%M:%S"), 'alice@example.com'),
        ('media/hayden.jpg', 'Met Hayden Christensen!', 'He was more handsome irl!', (now - timedelta(days=1)).strftime("%d/%m/%Y, %H:%M:%S"), 'bob@example.com'),
        ('media/sample3.jpg', 'Sad boy keeps being sad', 'Golden hour never disappoints.', (now - timedelta(days=2)).strftime("%d/%m/%Y, %H:%M:%S"), 'charlie@example.com'),
        ('media/sample4.jpg', 'NITRO', 'Tried a new blend at my favorite café.', (now - timedelta(days=3)).strftime("%d/%m/%Y, %H:%M:%S"), 'diana@example.com'),
        ('media/sample5.jpg', 'Sung Jingwoo aura farming... again', 'My top 5 books this year.', (now - timedelta(days=4)).strftime("%d/%m/%Y, %H:%M:%S"), 'edward@example.com'),
        ('media/nature.jpg', 'Stunning view', 'Truly amazing.', (now - timedelta(days=5)).strftime("%d/%m/%Y, %H:%M:%S"), 'fiona@example.com'),
        ('media/fish.jpg', 'Turned into a fish. Now what?', 'The caption says it all...', (now - timedelta(days=6)).strftime("%d/%m/%Y, %H:%M:%S"), 'george@example.com'),
        ('media/RTX.jpg', 'Just got new RTX 5090!', 'Super expensive, but performance is crazy!', (now - timedelta(days=7)).strftime("%d/%m/%Y, %H:%M:%S"), 'hannah@example.com'),
        ('media/sample9.jpg', 'Nitro update', 'Tunes that got me through the week.', (now - timedelta(days=8)).strftime("%d/%m/%Y, %H:%M:%S"), 'ian@example.com'),
        ('media/sample10.jpg', 'Girl met alien, never returned', 'Organized my desk and it feels amazing.', (now - timedelta(days=9)).strftime("%d/%m/%Y, %H:%M:%S"), 'julia@example.com')
    ]
    cursor.executemany("INSERT INTO blog (image, title, body, datetime, author) VALUES (?, ?, ?, ?, ?)", blogs)

    # Insert sample comments
    comments = [
        ('1', 'Love the forest vibes!', now.strftime("%d/%m/%Y, %H:%M:%S"), 'bob@example.com'),
        ('1', 'That looks peaceful.', now.strftime("%d/%m/%Y, %H:%M:%S"), 'charlie@example.com'),
        ('2', 'The city at night is stunning!', now.strftime("%d/%m/%Y, %H:%M:%S"), 'alice@example.com'),
        ('3', 'Wish I was there!', now.strftime("%d/%m/%Y, %H:%M:%S"), 'diana@example.com'),
        ('4', 'Which café is this?', now.strftime("%d/%m/%Y, %H:%M:%S"), 'fiona@example.com'),
        ('5', 'Adding those books to my list.', now.strftime("%d/%m/%Y, %H:%M:%S"), 'george@example.com'),
        ('6', 'Your painting is amazing!', now.strftime("%d/%m/%Y, %H:%M:%S"), 'hannah@example.com'),
        ('7', 'Italy is on my bucket list!', now.strftime("%d/%m/%Y, %H:%M:%S"), 'ian@example.com'),
        ('8', 'Max is adorable!', now.strftime("%d/%m/%Y, %H:%M:%S"), 'julia@example.com'),
        ('9', 'Great taste in music!', now.strftime("%d/%m/%Y, %H:%M:%S"), 'edward@example.com')
    ]
    cursor.executemany("INSERT INTO comment (post_id, comment, datetime, author) VALUES (?, ?, ?, ?)", comments)

    # Insert sample followers
    followers = [
        ('bob@example.com', 'alice@example.com'),
        ('charlie@example.com', 'alice@example.com'),
        ('diana@example.com', 'bob@example.com'),
        ('edward@example.com', 'charlie@example.com'),
        ('fiona@example.com', 'diana@example.com'),
        ('george@example.com', 'edward@example.com'),
        ('hannah@example.com', 'fiona@example.com'),
        ('ian@example.com', 'george@example.com'),
        ('julia@example.com', 'hannah@example.com'),
        ('alice@example.com', 'ian@example.com')
    ]
    cursor.executemany("INSERT OR IGNORE INTO followers (follower, following) VALUES (?, ?)", followers)

    # Insert sample likes (post likes)
    likes = [
        ('bob@example.com', 1, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('charlie@example.com', 1, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('alice@example.com', 2, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('diana@example.com', 3, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('fiona@example.com', 4, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('george@example.com', 5, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('hannah@example.com', 6, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('ian@example.com', 7, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('julia@example.com', 8, None, now.strftime("%d/%m/%Y, %H:%M:%S")),
        ('edward@example.com', 9, None, now.strftime("%d/%m/%Y, %H:%M:%S"))
    ]
    cursor.executemany("INSERT INTO likes (username, post_id, comment_id, created_at) VALUES (?, ?, ?, ?)", likes)

    conn.commit()
    conn.close()
    print("Database seeded with detailed sample data.")

def clear_blog_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM blog")
    conn.commit()
    conn.close()
    print("All records from the 'blog' table have been deleted.")

def clear_users_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    print("All records from the 'users' table have been deleted.")

def clear_comments_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM comment")
    conn.commit()
    conn.close()
    print("All records from the 'comment' table have been deleted.")

def clear_likes_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM likes")
    conn.commit()
    conn.close()
    print("All records from the 'likes' table have been deleted.")

def clear_followers_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM followers")
    conn.commit()
    conn.close()
    print("All records from the 'followers' table have been deleted.")

if __name__ == "__main__":
    clear_blog_table()
    clear_users_table()
    clear_likes_table()
    clear_followers_table()
    clear_comments_table()
    seed_database()