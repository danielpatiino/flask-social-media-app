# This is where all the Flask routes and main logic for BookRivals live.
# It handles stuff like login, signup, posting, editing, deleting, following, liking, and all the AJAX endpoints.
# This is where the main functionality of the app is implemented, connecting the frontend with the database and handling user interactions.

from flask import Blueprint, render_template, request, redirect, session, jsonify, send_from_directory, current_app
from models import fetch_all_blog_posts, add_admin_user, getPost
import re
import os
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from utils import get_follower_count, get_like_count, is_following, is_liked

DATABASE = "database.db"

routes = Blueprint('routes', __name__)

@routes.route('/')
def main():
    add_admin_user()
    if 'username' in session:
        posts = fetch_all_blog_posts()
        return render_template('main.html', posts=posts)
    return redirect('/login')

# Add other routes here, e.g., login, signup, follow, unfollow, etc.

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Server-side validation
        if not username or not password:
            return "Email and password are required. <a href='/login'>Try again</a>"

        if len(username) < 3 or len(password) < 8:
            return "Email must be at least 3 characters and password at least 8 characters long. <a href='/login'>Try again</a>"

        if not '@' in username or '.' not in username:
            return "Email must contain @ and (.)<a href='/login'>Try again</a>"

        if not re.match("^[a-zA-Z0-9_.@]+$", username):
            return "Email can only contain letters, numbers, dot and underscores. <a href='/login'>Try again</a>"

        # Fix regex: single backslash for \W, and test with raw string
        if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[\W_])(?=.*[0-9]).{8,}$", password):
            return "Password must contain at least 8 characters, 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character. <a href='/login'>Try again</a>"

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        # Fetch the hashed password from the database
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            session['username'] = username
            return redirect('/')
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>"

    user_agent = request.headers.get('User-Agent').lower()

    if "iphone" in user_agent or "android" in user_agent:
        return render_template('mobile_login.html')
    else:
        return render_template('login.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Server-side validation
        import re
        if not username or not password:
            return render_template('signup.html', error="Username and password are required.")
        if len(username) < 3:
            return render_template('signup.html', error="Username must be at least 3 characters.")
        if not ('@' in username and '.' in username):
            return render_template('signup.html', error="Username must be a valid email address.")
        if not re.match("^[a-zA-Z0-9_.@]+$", username):
            return render_template('signup.html', error="Username contains invalid characters.")
        if len(password) < 8:
            return render_template('signup.html', error="Password must be at least 8 characters.")
        if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[\W_])(?=.*[0-9]).{8,}$", password):
            return render_template('signup.html', error="Password must contain uppercase, lowercase, number, and special character.")

        # Hash the password for security
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            return redirect('/login')
        except sqlite3.IntegrityError:
            return render_template('signup.html', error="Username already exists. Please choose a different one.")

    return render_template('signup.html')

@routes.route('/add-item', methods=['POST'])
def add_item():
    if 'username' not in session:
        return redirect('/')

    if request.method == 'POST':
        file = request.files['image']
        title = request.form['title']
        body = request.form['body']

        date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        user = session['username']
        image = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO blog (image, title, body, datetime, author) VALUES (?, ?, ?, ?, ?)", (image, title, body, date_time, user))
            conn.commit()
            conn.close()
            return redirect('/')
        except sqlite3.IntegrityError:
            return "Some error occurred"

    return render_template('main.html', status=201)

@routes.route('/delete/<id>', methods=['GET'])
def delete(id):
    if 'username' not in session:
        return redirect('/')

    post = getPost(id)
    if post[5] == session['username']:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM blog WHERE id=?", (id,))
            conn.commit()
            conn.close()
            return redirect('/')
        except sqlite3.Error:
            return "Error occurred while deleting the post"
    else:
        return "Unauthorized access"

@routes.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if 'username' not in session:
        return redirect('/')

    if request.method == 'POST':
        file = request.files['image']
        title = request.form['title']
        body = request.form['body']

        if file.filename != '':
            image = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            if file.filename != '':
                cursor.execute("UPDATE blog SET image=?, title=?, body=? WHERE id=?", (image, title, body, id))
            else:
                cursor.execute("UPDATE blog SET title=?, body=? WHERE id=?", (title, body, id))
            conn.commit()
            conn.close()
            return redirect('/')
        except sqlite3.IntegrityError:
            return "Some error occurred"
    else:
        post = getPost(id)
        if post[5] == session['username']:
            return render_template('edit.html', post=post, status=200)
        else:
            return "Unauthorized access"

@routes.route('/details/<id>', methods=['GET', 'POST'])
def details(id):
    if 'username' not in session:
        return redirect('/')

    post = getPost(id)
    if post:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT comment, datetime, author FROM comment WHERE post_id = ?", (id,))
        comments = cursor.fetchall()
        conn.close()
        return render_template('details.html', post=post, comments=comments, status=201)
    else:
        return "Post not found", 404

@routes.route('/add-comment/<id>', methods=['POST'])
def add_comment(id):
    if 'username' not in session:
        return redirect('/')

    if request.method == 'POST':
        comment = request.form['comment']
        date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        user = session['username']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO comment (post_id, comment, datetime, author) VALUES (?, ?, ?, ?)", (id, comment, date_time, user))
            conn.commit()
            conn.close()
            return redirect(f'/details/{id}')
        except sqlite3.IntegrityError:
            return "Some error occurred"

    return render_template('main.html')

@routes.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return redirect('/')

    posts = fetch_all_blog_posts()  # Assuming this function fetches all posts
    matching_posts = [post for post in posts if query.lower() in post[1].lower() or query.lower() in post[2].lower()]

    return render_template('main.html', posts=matching_posts, search_query=query)

@routes.route('/toggle-like/<int:post_id>', methods=['POST'])
def toggle_like(post_id):
    if 'username' not in session:
        return jsonify({"success": False, "message": "User not logged in."}), 401

    username = session['username']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the user already liked the post
    cursor.execute("SELECT * FROM likes WHERE post_id = ? AND username = ?", (post_id, username))
    like = cursor.fetchone()

    if like:
        # Unlike the post
        cursor.execute("DELETE FROM likes WHERE post_id = ? AND username = ?", (post_id, username))
        liked = False
    else:
        # Like the post
        cursor.execute("INSERT INTO likes (post_id, username) VALUES (?, ?)", (post_id, username))
        liked = True

    # Get the updated like count
    cursor.execute("SELECT COUNT(*) FROM likes WHERE post_id = ?", (post_id,))
    like_count = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return jsonify({"success": True, "like_count": like_count, "liked": liked})

@routes.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect('/login')

    username = request.args.get('user')
    if not username:
        username = session['username']

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if request.method == 'POST' and username == session['username']:
        bio = request.form.get('bio')
        date_of_birth = request.form.get('date_of_birth')
        profile_picture = request.files.get('profile_picture')

        if profile_picture:
            picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], profile_picture.filename)
            profile_picture.save(picture_path)
            cursor.execute("UPDATE users SET profile_picture = ? WHERE username = ?", (picture_path, session['username']))

        cursor.execute("UPDATE users SET bio = ?, date_of_birth = ? WHERE username = ?", (bio, date_of_birth, session['username']))
        conn.commit()

    cursor.execute("SELECT username, profile_picture, bio, date_of_birth FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    # Get followers and following lists with counters
    cursor.execute("SELECT follower FROM followers WHERE following = ?", (username,))
    followers = cursor.fetchall()
    cursor.execute("SELECT following FROM followers WHERE follower = ?", (username,))
    following = cursor.fetchall()
    conn.close()

    followers_list = [f[0] for f in followers]
    following_list = [f[0] for f in following]

    if not user:
        return "User not found", 404

    return render_template('profile.html', user=user, followers=followers_list, following=following_list)

@routes.route('/follow/<username>', methods=['POST'])
def follow_user(username):
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    follower = session['username']
    if follower == username:
        return jsonify({'success': False, 'message': 'Cannot follow yourself'}), 400
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT OR IGNORE INTO followers (follower, following) VALUES (?, ?)", (follower, username))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Followed successfully'})
    except Exception as e:
        conn.close()
        return jsonify({'success': False, 'message': str(e)}), 500

@routes.route('/unfollow/<username>', methods=['POST'])
def unfollow_user(username):
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    follower = session['username']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM followers WHERE follower=? AND following=?", (follower, username))
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': 'Unfollowed successfully'})
    except Exception as e:
        conn.close()
        return jsonify({'success': False, 'message': str(e)}), 500

@routes.route('/api/follower-count/<username>')
def api_follower_count(username):
    count = get_follower_count(username)
    return jsonify({'count': count})

@routes.route('/user-directory')
def user_directory():
    if 'username' not in session:
        return redirect('/login')
    import sqlite3
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, profile_picture, bio FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('user_directory.html', users=users)
