FROM python:3.13.5-slim

WORKDIR /app

COPY tools/requirements/req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT settings.wsgi:application"]
