# Simple Server for recieving JSONs

Перед запуском склонируйте проект:
```
git clone https://github.com/auplt/SimpleServer.git
```

## Общая информация
- Приложение использует фреймворк flask
- Установка flask
```
pip install Flask
```
- Сервер использует local host по адресу 127.0.0.1:5000

## Запуск проекта

### Создание окружения
```
venv\Scripts\activate
```
Задание переменной окружения (Windows)
```
set FLASK_APP=main.py
```

### Запуск сервера
```
flask run
```