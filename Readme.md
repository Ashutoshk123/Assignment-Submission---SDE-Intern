# Alerting_Platform

A Django-based alerting platform for managing alerts, escalations, and dashboards. This README provides quick start instructions (Windows PowerShell), project structure, configuration, and common operational tasks.

## Features
- User authentication and admin interface
- Alert creation and management
- Escalation flow tracking (e.g., `alert_escalated` flags)
- Basic dashboard and static assets under `core/static/core`
- Django ORM with SQLite (default)

## Tech Stack
- Python 3.11+ (recommended)
- Django 5.x (project layout suggests modern Django)
- SQLite (dev default)

## Project Structure
```
alerting_platform/
  config/               # Project settings, URLs, ASGI/WSGI
  core/                 # Main app: models, views, templates, static
    static/core/        # CSS and static assets
    templates/core/     # HTML templates (add your pages here)
  db.sqlite3            # Dev database (autocreated)
  manage.py             # Django management CLI
Readme.md
```

## Prerequisites
- Windows 10/11 with PowerShell
- Python installed and added to PATH (`python --version`)
- Optional: Git

## Quick Start (Windows PowerShell)
```powershell
# 1) Go to project root
cd "C:\Users\ashut\OneDrive\Desktop\Assignment"

# 2) Create and activate a virtual environment
python -m venv .venv
. .venv\Scripts\Activate.ps1

# 3) Upgrade pip
python -m pip install --upgrade pip

# 4) Install dependencies
# If requirements.txt is missing, this will create it with minimal pins.
if (!(Test-Path requirements.txt)) {
  @(
    "Django>=5.0,<6.0"
  ) | Out-File -Encoding utf8 requirements.txt
}
pip install -r requirements.txt

# 5) Apply migrations
python manage.py migrate

# 6) Create a superuser (follow prompts)
python manage.py createsuperuser

# 7) Run the development server
python manage.py runserver 0.0.0.0:8000
```

Then open `http://127.0.0.1:8000/` for the app and `http://127.0.0.1:8000/admin/` for the admin panel.

## Environment Configuration
Django settings live in `alerting_platform/config/settings.py`.

- **Secret key**: For production, set `DJANGO_SECRET_KEY` (and load it in settings) or replace the default.
- **Debug**: Set `DEBUG=0` for production.
- **Allowed hosts**: Add your domains/IPs to `ALLOWED_HOSTS`.
- **Database**: Default is SQLite. To use Postgres, set `DATABASES` in `settings.py` or via `DATABASE_URL` with `dj-database-url`.

Example `.env` (optional):
```
DJANGO_SECRET_KEY=replace-me
DEBUG=1
ALLOWED_HOSTS=127.0.0.1,localhost
```
You can load `.env` with `python-dotenv` or integrate in `settings.py`.

## Managing the App
- Make migrations after model changes:
  ```powershell
  python manage.py makemigrations
  python manage.py migrate
  ```
- Collect static files (when preparing for production):
  ```powershell
  python manage.py collectstatic --noinput
  ```
- Run tests (if/when added under `core/tests.py`):
  ```powershell
  python manage.py test
  ```

## Key Modules
- `alerting_platform/core/models.py`: Alert models, escalation flags, timestamps
- `alerting_platform/core/views.py`: Views for dashboard and alert operations
- `alerting_platform/config/urls.py`: Routes for core app and admin
- `alerting_platform/core/templates/core/`: HTML templates

## Data Model
Migrations present:
- `0001_initial.py`: Base schema for alerts and related entities
- `0002_alert_cron_schedule_alert_escalated_and_more.py`: Adds scheduling, escalation, and related fields

Inspect models in `core/models.py` for authoritative structure.

## Common Workflows
- Add a new page: create template in `core/templates/core`, add view in `core/views.py`, wire URL in `config/urls.py`.
- Modify styles: edit CSS in `core/static/core/*.css`; ensure `STATIC_URL`/`STATICFILES_DIRS` are configured.
- Admin customization: register models in `core/admin.py`.

## Deployment Notes
- Set `DEBUG=0`, configure `ALLOWED_HOSTS`.
- Switch to Postgres or other RDBMS.
- Set a strong `SECRET_KEY` via environment.
- Serve static files via `collectstatic` and a proper web server (e.g., Nginx) or a CDN.
- Use `gunicorn`/`uvicorn` with ASGI/WSGI as appropriate.

## Troubleshooting (Windows)
- Activate venv fails: run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` in an elevated PowerShell, then re-run activation.
- Port in use: change to another port, e.g., `python manage.py runserver 0.0.0.0:8001`.
- Migration conflicts: delete `db.sqlite3` in dev only, then re-run `migrate` (you will lose data).
- Static files not loading: ensure `DEBUG=1` in dev, check `STATIC_URL` and app `INSTALLED_APPS` include `django.contrib.staticfiles`.


## Acknowledgements
Built with Django.



