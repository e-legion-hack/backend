# e-legion-backend

## How to run

The fastest way to run is to run it using SQLite database without all Celery workers for background jobs. This should be enough for quickstart:

``` bash
git clone https://github.com/e-legion-hack/e-legion-backend.git
cd e-legion-backend
```

Create virtual environment (optional)
``` bash
python3 -m venv e_legion_venv
source e_legion_venv/bin/activate
```

Install all requirements:
```
pip install -r requirements.txt
```

Create `.env` file in root directory and copy-paste this:
``` bash 
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Run migrations to setup SQLite database:
``` bash
python manage.py migrate
```

Create superuser to get access to admin panel:
``` bash
python manage.py createsuperuser
```

If you want to open Django admin panel which will be located on http://localhost:8000/legionadmin/:
``` bash
python manage.py runserver
```
