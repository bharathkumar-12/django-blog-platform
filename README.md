# Blog Application

Modern Django blog with clean UI, pagination, search, and tags.

## Features

- Responsive Tailwind UI
- Pagination and search
- Tags
- Clean templates and CBVs

## Requirements

- Python 3.12
- Django 5.0+
- SQLite (default)

## Local Development

1. Clone the repo.
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`.
4. Copy `.env.example` to `.env` and set values.
5. Run migrations: `python manage.py migrate`.
6. Create a superuser: `python manage.py createsuperuser`.
7. Run the server: `python manage.py runserver`.

## Environment Variables

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

## Deployment (Heroku or compatible)

1. Set environment variables in the platform.
2. Ensure `runtime.txt` matches your Python version.
3. Deploy and run migrations.

## Screenshots

Add screenshots to `docs/screenshots` and update this section.

## Security

- Never commit secrets or credentials.
- Use environment variables for all sensitive settings.
