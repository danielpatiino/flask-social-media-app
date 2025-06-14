// This is the main JavaScript file for BookRivals. 
// Handles form validation, AJAX for likes/follows, dark mode, modals, and all the interactive stuff.

// This function fetches comments for a post using AJAX (fetch API)
function fetchComments(postId) {
	fetch('/get-comments/' + postId)
		.then(response => response.json())
		.then(comments => {
			document.getElementById('comments-' + postId).innerHTML = '';
			comments.forEach(comment => {
				document.getElementById('comments-' + postId).innerHTML += '<div><hr>'+comment[2]+'  <br>postedAt <b>' +comment[3]+'</b><br>  postedBy <b>' +comment[4]+'</b></div>';
			});
		})
		.catch(error => console.error('Error fetching comments:', error));
}

// Here we set up the modal for viewing a blog post
var modal = document.getElementById("myModal");
var btn = document.getElementById("openModal");
var span = document.getElementsByClassName("close")[0];

// When you click the button, the modal pops up
btn.onclick = function() {
  modal.style.display = "block";
}

// If you click the X, the modal closes
span.onclick = function() {
  modal.style.display = "none";
}

// If you click outside the modal, it also closes
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// This function lets you like or unlike a post, and updates the like count right away
function toggleLike(postId) {
    fetch(`/toggle-like/${postId}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            const likeButton = document.querySelector(`button[onclick="toggleLike('${postId}')"]`);
            const likeCountSpan = likeButton.querySelector('span');
            if (data.success) {
                likeCountSpan.textContent = data.like_count;
                // Change the heart icon and button style depending on if you liked it or not
                if (data.liked) {
                    likeButton.classList.remove('btn-outline-primary');
                    likeButton.classList.add('btn-primary');
                    likeButton.innerHTML = '❤️ <span>' + data.like_count + '</span>';
                } else {
                    likeButton.classList.remove('btn-primary');
                    likeButton.classList.add('btn-outline-primary');
                    likeButton.innerHTML = '♥ <span>' + data.like_count + '</span>';
                }
            } else {
                alert(data.message || 'Error toggling like.');
            }
        })
        .catch(error => {
            alert('Error: ' + error);
        });
}

// Checks if the login form is filled out correctly before sending it
function validateLoginForm(event) {
    const email = document.querySelector('input[name="username"]').value;
    const password = document.querySelector('input[name="password"]').value;

    if (!email || !password) {
        alert('Email and password are required.');
        event.preventDefault();
        return false;
    }

    const emailPattern = /^[a-zA-Z0-9_.@]+$/;
    if (!emailPattern.test(email)) {
        alert('Email can only contain letters, numbers, dots, and underscores.');
        event.preventDefault();
        return false;
    }

    const passwordPattern = /^(?=.*[A-Z])(?=.*[\W_])(?=.*[0-9]).{8,}$/;
    if (!passwordPattern.test(password)) {
        alert('Password must contain at least 8 characters, including 1 uppercase letter, 1 special character, and 1 digit.');
        event.preventDefault();
        return false;
    }

    return true;
}

// Checks if the signup form is filled out correctly before sending it
function validateSignupForm(event) {
    const email = document.querySelector('input[name="username"]').value;
    const password = document.querySelector('input[name="password"]').value;

    if (!email || !password) {
        alert('Email and password are required.');
        event.preventDefault();
        return false;
    }

    const emailPattern = /^[a-zA-Z0-9_.@]+$/;
    if (!emailPattern.test(email)) {
        alert('Email can only contain letters, numbers, dots, and underscores.');
        event.preventDefault();
        return false;
    }

    const passwordPattern = /^(?=.*[A-Z])(?=.*[\W_])(?=.*[0-9]).{8,}$/;
    if (!passwordPattern.test(password)) {
        alert('Password must contain at least 8 characters, including 1 uppercase letter, 1 special character, and 1 digit.');
        event.preventDefault();
        return false;
    }

    return true;
}

// This one toggles dark mode on and off, and remembers your choice
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');

    // Save the user's preference in localStorage
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
}

// When the page loads, we check if you wanted dark mode, and set up event listeners for forms and dark mode button
window.onload = function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }

    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', toggleDarkMode);
    }

    // Attach existing event listeners
    const loginForm = document.querySelector('form[action="/login"]');
    if (loginForm) {
        loginForm.addEventListener('submit', validateLoginForm);
    }

    const signupForm = document.querySelector('form[action="/signup"]');
    if (signupForm) {
        signupForm.addEventListener('submit', validateSignupForm);
    }
};