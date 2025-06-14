# BookRivals: A Social Platform

BookRivals is a social media web app built with Flask and Bootstrap. You can share posts, follow friends, browse users, and just hang out in a modern, responsive design. It’s made to be easy to use, and has all the features you’d expect from a proper social platform.

## Functionality

- Log in and register users  
  (passwords are hashed and stored safely in the database; check out `routes.py` and `models.py`)

- Example data  
  (the app comes with some users, posts, and comments already, so you can test stuff right away; see `setup.py`. The database is already pre-seeded, so you do not need to run any extra script.)

- JS form validation  
  (custom JavaScript in `static/script.js` checks if you typed your email and password right, and gives you clear error messages if not)

- Search posts  
  (search for blog posts by title or content; see the `/search` route in `routes.py`)

- Preference stored  
  (dark mode is saved in your browser, so it stays even if you reload with localStorage; see `static/script.js`)

- Update, delete data  
  (you can edit or delete your own blog posts; see `/edit/<id>`, `/delete/<id>` in `routes.py`)

- AJAX requests used  
  (likes, follow/unfollow, and follower count update instantly without reloading; see `static/script.js` and the routes)

- Fluid layout  
  (the layout adapts to any screen size thanks to Bootstrap and some custom CSS)

- Absolute positioning used  
  (modals and some overlays use absolute positioning; see the modal in `base.html` and the CSS)

- Flex used  
  (post grids and some layouts use flexbox, both with Bootstrap and custom CSS)

- Semantic tags  
  (HTML templates use tags like `<main>`, `<header>`, `<footer>`, `<nav>`, etc. for better structure)

- Bootstrap-based layout and responsive design  
  (Bootstrap is used everywhere for grid, layout, and making things look good on all devices)

- Phone layout  
  (the app works great on your phone, also on desktop; see media queries in `static/style.css`)

- Code separation  
  (the code is split into `models.py`, `routes.py`, `utils.py`, etc. so it’s easier to work with)

- Data stored  
  (everything is in SQLite, with 5 tables: users, blog, comment, followers, likes; see `models.py`)

- REST API  
  (AJAX endpoints like `/toggle-like/<post_id>`, `/follow/<username>`, `/unfollow/<username>`, and `/api/follower-count/<username>` use REST-style naming and return JSON)

- Server-side validation  
  (all form inputs are checked on the server too, not just in the browser; see `routes.py`)

- Errors handled and displayed  
  (If something goes wrong, you always get a clear error message. Like, if you mess up a form, the site tells you what’s wrong right away. If you try to like or follow and it fails, you see an alert. The backend also checks stuff and sends back good error messages and codes, so you know if you’re not allowed to do something or if a file upload fails. All this is in `routes.py` and `static/script.js`.)

- Authentication  
  (you have to be logged in to use the main features; session stuff is in `routes.py`)

- Access control  
  (only you can edit or delete your own posts, and you can only follow/unfollow others; enforced in `routes.py`)


### Extra Features

- Profile picture upload and display for users  
  (You can upload a profile pic from your profile page, and it shows up everywhere your name does. The images are saved in the `media/` folder. Check out `routes.py` and `models.py` for how it works.)

- Image upload for blog posts  
  (When you make a post, you can add a picture if you want. It gets saved and shown with your post. See `routes.py`, `models.py`, and `main.html`.)

- Real-time like and follow/unfollow updates  
  (When you like a post or follow someone, it updates instantly—no need to reload. That's all done with JavaScript and some Flask routes.)

- Modal popup for adding new posts  
  (Instead of going to a new page, you just click 'Add Post' and a popup appears. Makes it way faster to post stuff. See `main.html` and `static/script.js`.)

- Password strength enforced  
  (You can't just use '1234' as a password. The app checks if your password is strong enough, both in the browser and on the server. See `static/script.js` and `routes.py`.)

- Follower/following lists on profile page  
  (On your profile, you can see who follows you and who you follow, with links to their profiles. It's all in `profile.html` and `routes.py`.)

- Visual feedback for like/unlike  
  (When you like a post, the button changes right away so you know it worked. That's handled in the JavaScript and `main.html`.)

- Admin user always available  
  (There's always an admin user in the database, so you can't get locked out. Made in `setup.py`.)

- User-friendly date/time formatting for posts and comments  
  (Instead of weird timestamps, you see stuff like '2 hours ago' on posts and comments. That's done in the backend and shown in `main.html`.)

- Responsive cards and grid for posts  
  (Posts are shown in nice cards that fit any screen size, thanks to Bootstrap and some CSS tweaks. See `main.html` and `static/style.css`.)

- Truncated post titles for better UI  
  (If a post title is super long, it gets shortened with '...' so the layout doesn't break. That's in the JavaScript and `main.html`.)

- Custom error messages for form validation  
  (If you mess up a form, you'll get a clear message about what went wrong, both from the browser and the server. See `static/script.js` and `routes.py`.)


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


## Structure

- app.py              — Flask entry point
- models.py           — Database models
- routes.py           — App routes and logic
- utils.py            — Helpers
- setup.py            — Example data
- update_schema.py    — Schema updates
- media/              — Uploaded images
- static/             — CSS, JS
- templates/          — HTML templates


## About

Made for the DAT310 web programming project. Hope you enjoy using it!
