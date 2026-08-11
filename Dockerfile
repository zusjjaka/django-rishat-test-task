FROM python:3.13.5-slim

WORKDIR /app

COPY tools/requirements/req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "settings.wsgi:application"]
