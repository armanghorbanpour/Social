<div align="center">

# Social

### A text-based social networking web application built with Django

A web application where users can publish text posts, discover content, interact through likes and comments, reply to discussions, and connect with other users.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.7-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)

</div>

---

## Overview

**Social** is a text-focused social networking project developed with **Python and Django**. It provides the core features needed for users to create an account, publish and manage posts, interact with other users, and take part in conversations.

The project includes account management, user profiles, a follow system, post search, likes, threaded comments and replies, and password recovery through email.

The interface is built with Django templates, Bootstrap, and custom CSS. It is responsive and designed around readable text content rather than image-first posts.

## Features

### Accounts and authentication
- User registration with username, email, password, and password confirmation.
- Form validation for duplicate usernames and email addresses.
- Login using account credentials, with support for the configured email authentication backend.
- Logout functionality.
- Password reset flow using email.
- Login-required access to protected actions and pages.

### User profiles
- A profile is automatically created when a new user account is created.
- View user profiles and their published posts.
- Edit profile information, including email, age, and bio.
- Follow and unfollow other users.

### Posts
- Create text-based posts.
- View posts on the home page.
- Open a dedicated page for each post.
- Edit and delete your own posts.
- Search posts by their text content.
- Display posts in reverse chronological order.

### Engagement and discussions
- Like posts.
- Display the number of likes on a post.
- Prevent the same user from liking the same post more than once.
- Add comments to posts.
- Reply to existing comments.
- Display replies as part of the related discussion.

### Interface and usability
- Responsive layout using Bootstrap.
- Custom styling with CSS.
- Shared base template and reusable navigation/messages components.
- Django messages for feedback after user actions.
- Automatic dismissal of notification messages after a short delay.
- Collapsible reply forms to keep discussions uncluttered.

### Administration
- Django Admin integration for site administration.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django 5.0.7 | Web framework, routing, views, forms, authentication, and ORM |
| SQLite | Development database |
| HTML5 | Page structure |
| CSS3 | Custom interface styling |
| Bootstrap 5 | Responsive layout and UI components |
| JavaScript | Small interface interactions, including dismissible alerts |
| Django Templates | Server-rendered frontend |

## Project Structure

The repository contains the Django project inside the `A/` directory.

```text
social/
└── A/
    ├── A/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── account/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── account/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── authentication.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── signals.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── home/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── home/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── static/
    │   └── css/
    │       └── style.css
    │
    ├── templates/
    │   ├── inc/
    │   │   ├── messages.html
    │   │   └── navbar.html
    │   └── base.html
    │
    ├── db.sqlite3
    └── manage.py
```

### Django apps

- **`home`** — post creation and management, home feed, search, likes, comments, and replies.
- **`account`** — registration, login, logout, profiles, profile editing, follow relationships, email authentication, and password reset.
- **`A`** — main Django project configuration, settings, and root URL configuration.

## Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/armanGitCourse/social.git
cd social
```

### 2. Create and activate a virtual environment

Create the virtual environment in the repository root.

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install project dependencies

Install the required packages from the requirements file:

```bash
pip install -r requirements.txt
```

### 4. Configure environment-specific settings

Review `A/A/settings.py` and configure the values required for your local environment.

- Use a private Django `SECRET_KEY`.
- Keep `DEBUG` enabled only for local development.
- Configure `ALLOWED_HOSTS` appropriately.
- Configure SMTP credentials if you want email-based password reset to work.
- Never commit passwords, email app passwords, secret keys, or other credentials to the repository.

Use environment variables for sensitive configuration.

### 5. Open the Django project directory

The Django project and `manage.py` are inside the `A/` directory:

```bash
cd A
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account (optional)

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open the application at `http://127.0.0.1:8000/`.

The Django administration panel is available at `http://127.0.0.1:8000/admin/`.

## Main Application Routes

| Route | Description |
|---|---|
| `/` | Home feed and post search |
| `/post/<post_id>/<post_slug>` | Post details, likes, comments, and replies |
| `/post/create` | Create a post |
| `/post/update/<post_id>/` | Update a post |
| `/post/delete/<post_id>/` | Delete a post |
| `/like/<post_id>/` | Like a post |
| `/reply/<post_id>/<comment_id>` | Reply to a comment |
| `/account/register/` | Create an account |
| `/account/login/` | Log in |
| `/account/logout/` | Log out |
| `/account/profile/<user_id>/` | View a user profile |
| `/account/edit_user/` | Edit your profile |
| `/account/follow/<user_id>/` | Follow a user |
| `/account/unfollow/<user_id>/` | Unfollow a user |
| `/account/reset/` | Start password recovery |
| `/admin/` | Django administration |

> Some actions require authentication. The application uses Django's authentication system and login-required views for protected functionality.

## Data Models

The project uses Django models to represent its main application data.

### `Post`
Stores text posts and their author, slug, creation time, and last update time.

### `Comment`
Stores comments associated with a post and user. A self-referencing relationship allows comments to have replies.

### `Vote`
Stores a user's like on a post.

### `Profile`
Stores additional user information such as age and bio. A one-to-one relationship connects each profile to a Django user.

### `Relation`
Represents a follow relationship between two users.

## Email Configuration

The password recovery workflow uses Django's email functionality. To use it locally, configure an SMTP provider in the Django settings.

For Gmail SMTP, the typical configuration uses:
- SMTP host: `smtp.gmail.com`
- Port: `587`
- TLS: enabled
- A dedicated app password where required by the account's security settings

**Never put real email credentials or app passwords in source code or commit them to Git.** Configure them through environment variables or another private configuration method.

## Current Scope

This repository documents the features implemented so far. The current application is focused on text posts and user interaction.


## Development Notes

- The frontend uses Django's server-rendered template system.
- SQLite is configured as the development database.
- Database schema changes are tracked through Django migrations.
- The project is organized into separate `home` and `account` apps to keep post-related and user-related functionality separated.
- Email-based password recovery depends on valid SMTP configuration.

## Contributing

Suggestions, bug reports, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application locally.
5. Open a pull request describing your changes.


---

<div align="center">

**Built with Python, Django, and a passion for web development.**

</div>
