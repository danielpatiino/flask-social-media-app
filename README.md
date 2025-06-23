BookRivals is a social media web app built with Flask and Bootstrap. You can share posts, follow friends, and interact—all in a modern, responsive design. It’s easy to use and includes the key features you'd expect from a proper social platform.

Functionality
Log in and register users
(Passwords are hashed and stored securely in the database; see routes.py and models.py.)

Preloaded demo data
(Test users, posts, and comments are already included; no extra setup required. See setup.py.)

Post and comment
(Share posts with optional images and leave comments. See main.html, routes.py, models.py.)

Search
(Search posts by title or content; see the /search route.)

Like and follow
(Like posts or follow users instantly with AJAX updates; handled in script.js and routes.py.)

Dark mode
(Saved in localStorage so it stays active after reload; see script.js.)

Responsive layout
(Looks great on phones and desktops using Bootstrap and custom CSS.)

Profile pages
(Users can upload profile pictures and see their posts, followers, and following lists.)

Edit and delete posts
(You can manage your own content only; see routes.py.)

Password strength check
(Passwords are validated on both client and server sides.)

Modal for new posts
(Click 'Add Post' to open a popup instead of navigating to another page.)

Developer Notes
Code separation
(routes.py, models.py, utils.py, etc. for clean structure.)

SQLite database
(Includes tables for users, posts, comments, likes, and followers.)

REST-style endpoints
(Like /toggle-like/<post_id>, /follow/<username>, returns JSON.)

Form validation
(Checked in both script.js and routes.py.)

Error handling
(Clear error messages are shown in the browser and returned from the backend.)

Authentication and access control
(Users must be logged in and can only manage their own content.)

Extra Features
Real-time UI feedback for like/follow
(Buttons update immediately after interaction.)

Always-available admin user
(Default admin account is included; see setup.py.)

Friendly date formatting
(Posts and comments show human-readable times like "2 hours ago.")

Responsive card layout
(Post previews are shown in flexible Bootstrap cards.)

Truncated long titles
(Very long titles are shortened to keep layout clean.)

Semantic HTML
(Uses tags like <main>, <nav>, <footer>, etc.)

Custom error messages
(Forms provide helpful validation feedback in the UI.)


## Requirements

- Python 3.10 or newer

- Flask, Werkzeug


## Usage

To run the app, just open a terminal and type:

```bash
python app.py
```

The app will run on http://127.0.0.1:8080

You can log in with the default user, or create your own:

- Email: admin1@gmail.com
- Password: Webrivals@123

#About

Enjoy!
