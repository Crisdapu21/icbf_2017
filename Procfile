web: gunicorn icbf.wsgi --log-file -
worker: celery -A icbf.celery worker --loglevel=info --concurrency=1
worker: celery -A icbf.celery worker --beat --loglevel=info --concurrency=1
