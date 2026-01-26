# Blog Application

A simple Django blog for creating and viewing posts.

## Local Development

1. Clone the repo.
2. Create virtual env: `python -m venv venv`.
3. Activate: `source venv/bin/activate`.
4. Install: `pip install -r requirements.txt`.
5. Copy `.env.example` to `.env` and set values.
6. Run migrations: `python manage.py migrate`.
7. Create a superuser: `python manage.py createsuperuser`.
8. Start: `python manage.py runserver`.

## Deployment (Heroku or compatible)

1. Set environment variables (SECRET_KEY, DEBUG, ALLOWED_HOSTS).
2. Ensure `runtime.txt` matches your Python version.
3. Deploy and run migrations.

## Security

- Never commit secrets or credentials.
- Use environment variables for all sensitive settings.
