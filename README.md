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

<img width="1337" height="705" alt="Screenshot 2026-01-26 at 11 06 19 AM" src="https://github.com/user-attachments/assets/07edbd47-49e5-457d-82e1-4d24133cc909" />
<img width="1337" height="705" alt="Screenshot 2026-01-26 at 11 06 29 AM" src="https://github.com/user-attachments/assets/cfd59051-6e9c-47a2-bc88-255690907100" />
<img width="343" height="608" alt="Screenshot 2026-01-26 at 11 12 57 AM" src="https://github.com/user-attachments/assets/36be2737-beee-4c34-ba85-4e83ccb26349" />

## Security

- Never commit secrets or credentials.
- Use environment variables for all sensitive settings.

---

## Maintenance

Last maintenance update: <!--LAST_UPDATED-->2026-05-19<!--/LAST_UPDATED-->
