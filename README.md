# 📚 BookRivals: Social Media Web App

BookRivals is a modern social media platform built with Flask and Bootstrap. Share posts, follow friends, and interact—all in a sleek, responsive design. 🚀

---

## ✨ Features

- **User Authentication**: Register and log in securely (passwords are hashed and stored safely).
- **Preloaded Demo Data**: Test users, posts, and comments included—no extra setup! (See `setup.py`)
- **Post & Comment**: Share posts (with optional images) and leave comments. (See `main.html`, `routes.py`, `models.py`)
- **Search**: Find posts by title or content (`/search` route).
- **Like & Follow**: Like posts or follow users instantly with AJAX (see `script.js`, `routes.py`).
- **Dark Mode**: Toggle dark mode—your preference is saved! (see `script.js`)
- **Responsive Layout**: Looks great on all devices (Bootstrap + custom CSS).
- **Profile Pages**: Upload profile pictures, view posts, followers, and following.
- **Edit & Delete Posts**: Manage your own content only (see `routes.py`).
- **Password Strength Check**: Validated on both client and server sides.
- **Modal for New Posts**: Add posts via popup modal.

---

## 🛠️ Developer Notes

- **Clean Code Structure**: Separated into `routes.py`, `models.py`, `utils.py`, etc.
- **SQLite Database**: Tables for users, posts, comments, likes, and followers.
- **RESTful Endpoints**: e.g., `/toggle-like/<post_id>`, `/follow/<username>` (returns JSON).
- **Form Validation**: Both client-side (`script.js`) and server-side (`routes.py`).
- **Error Handling**: Clear error messages in the UI and backend.
- **Authentication & Access Control**: Users manage only their own content.

---

## 🌟 Extra Features

- Real-time UI feedback for like/follow (instant button updates)
- Always-available admin user (see `setup.py`)
- Friendly date formatting (e.g., "2 hours ago")
- Responsive card layout for posts
- Truncated long titles for clean layout
- Semantic HTML (`<main>`, `<nav>`, `<footer>`, etc.)
- Custom error messages for forms

---

## 📦 Requirements

- Python 3.10 or newer
- Flask, Werkzeug

---

## 🚀 Usage

To run the app, open a terminal and type:

```bash
python app.py
```

The app will run at: [http://127.0.0.1:8080](http://127.0.0.1:8080)

**Default Admin Login:**
- Email: `admin1@gmail.com`
- Password: `Webrivals@123`

---

## 💡 About

Enjoy using BookRivals! 📖✨
