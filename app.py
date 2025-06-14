# Hey! This is the main Flask entry point for BookRivals. It sets up the app, loads config, and starts the server. 
# All the routes and logic are imported from routes.py. Super important for running the whole site.
from flask import Flask, send_from_directory
from routes import routes
from models import create_table_user, create_table_blog, create_table_comment, create_table_followers, create_table_likes
from utils import get_follower_count, get_like_count, is_following, is_liked, get_display_name
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'media'

# Initialize database tables
create_table_user()
create_table_blog()
create_table_comment()
create_table_followers()
create_table_likes()

@app.context_processor
def utility_processor():
    return dict(
        get_follower_count=get_follower_count,
        get_like_count=get_like_count,
        is_following=is_following,
        is_liked=is_liked,
        get_display_name=get_display_name
    )

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Register blueprints
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)