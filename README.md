# mysite

A Django-powered personal website and blog built with Python. This project includes a homepage, about page, contact form, blog posts with categories/tags, and sitemap/SEO-friendly configuration.

## Features

- Django 5.2 project structure
- Homepage and static pages (`about`, `contact`)
- Blog application with post listing, categories, tags, and search
- Contact form with validation and success/error messages
- Media and static file handling
- Sitemap support for blog and static pages
- Admin dashboard for content management
- Docker support for easy local deployment

## Tech Stack

- Python 3.12
- Django 5.2
- SQLite (default database)
- Pillow
- django-taggit
- django-simple-captcha
- django-summernote
- django-debug-toolbar
- django-robots

## Project Structure

```text
mysite/
├── blog/                    # Blog app
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── media/                   # Uploaded media files
├── mysite/                  # Project settings and URL routing
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── static/                 # Collected static files
├── statics/                # Static project assets
├── templates/               # Shared templates
├── web_app/                 # Main site app
│   ├── migrations/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
├── .gitignore
├── Dockerfile
├── LICENSE.md
├── manage.py
├── README.md
├── requirements.txt
└── db.sqlite3
```

## Requirements

Install Python dependencies with:

```bash
pip install -r requirements.txt
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/mahdi58git/mysite.git
cd mysite
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create an admin user:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## Docker

Build and run the application using Docker:

```bash
docker build -t mysite .
docker run -p 8000:8000 mysite
```

## Admin and Content

The project includes a Django admin interface where you can manage:

- blog posts
- categories
- tags
- user content
- contact submissions

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Notes

This repository is intended for development and local usage. The Django settings currently use `DEBUG = True` and SQLite, which is suitable for local development but should be adjusted for production deployment.
