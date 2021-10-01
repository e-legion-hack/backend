release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker e_legion.asgi:application
worker: celery -A e_legion worker -P prefork --loglevel=INFO
beat: celery -A e_legion beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
