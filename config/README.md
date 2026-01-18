# Secure Task Management System (Django)

## Project Description
A secure CRUD application built with Django for IKB21503 Secure Software Development. This system implements Task Management with a focus on OWASP Top 10 mitigation.

## Security Features Summary
- **Authentication**: Secure Login/Logout using Django's PBKDF2 hashing.
- **RBAC**: Role-Based Access Control for Admins vs Normal Users.
- **IDOR Protection**: Database queries are filtered by `request.user` to ensure users only access their own data.
- **Audit Logging**: Automatic logging of login attempts and CRUD activities.
- **CSRF Protection**: Tokens enforced on all POST requests.
- **XSS Mitigation**: Automatic output encoding via Django Template Engine.

## Installation & How to Run
1. Clone the repo: `git clone <your-repo-link>`
2. Create venv: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run Migrations: `python manage.py migrate`
6. Create Admin: `python manage.py createsuperuser`
7. Start App: `python manage.py runserver`

## Dependencies
- Django 4.x+
- Python 3.x