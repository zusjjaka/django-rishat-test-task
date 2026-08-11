# django-rishat-test-task

Тестовое задание на Django с интеграцией Stripe.

## Хостинг

https://django-rishat-test-task-production.up.railway.app/

## Реализовано

- Главная страница `/`
- Список товаров с возможностью собрать корзину `/item/`
- Страница товара с возможностью купить его `/item/<id>/`
- Создание Stripe Checkout Session для корзины `/buy/`
- Создание Stripe Checkout Session для товара `/buy/<id>/`
- Джанго админ панель `/admin/`
- Оплата через Stripe Checkout
- Поддержка USD и EUR валют
- Настройка через переменные окружения
- Docker контейнер
- Деплой на Railway
- Ruff для форматирования и проверки кода

## Стек

- Python 3.13.5
- Django
- Stripe
- Gunicorn
- WhiteNoise
- Docker
- Railway
- Ruff

## Запуск локально

### 1. Клонировать репозиторий

```bash
git clone https://github.com/zusjjaka/django-rishat-test-task/
cd django-rishat-test-task
```

### 2. Создать виртуальное окружение

Linux:

```bash
python3 -m venv env
source env/bin/activate
```

Windows:

```cmd
py -m venv env
.\env\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r tools/requirements/req.txt
```

### 4. Создать `.env` файл

Добавьте необходимые переменные окружения, используемые в `settings/base.py`, включая секретный ключ Django и ключи Stripe.

```.env
SECRET_KEY=*****
DEBUG=False
HOST=localhost
STRIPE_SEC_KEY=sk_test_*****
STRIPE_PUB_KEY=pk_test_*****
DB_NAME=postgres
DB_USER=postgres
DB_PASS=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Применить миграции

```bash
python3 manage.py migrate
```

### 6. Создать администратора

```bash
python manage.py createsuperuser
```

### 7. Запустить сервер

Для разработки:

```bash
python3 manage.py runserver
```

Для запуска через Gunicorn:

```bash
gunicorn --bind 127.0.0.1:8000 settings.wsgi:application
```

## Запуск через Docker

Собрать образ:

```bash
docker build -t django-rishat-test-task .
```

Собрать контейнер:

```bash
docker run -d \
    --name django-app \
    -p 8000:8000 \
    --env-file .env \
    -e PORT=8000 \
    django-rishat-test-task
```

Запустить контейнер:

```bash
docker start django-app
```

Остановить контейнер:

```bash
docker stop django-app
```

## Деплой

Проект подготовлен для деплоя на Railway.

Railway использует `Dockerfile` для сборки приложения.

Переменные окружения передаются через Variables.

Для запуска приложения используется Gunicorn.

## Форматирование и проверка кода

```bash
ruff check
```
