# Базовый образ с Python
FROM python:3.10

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app

# Указываем PYTHONPATH, чтобы Python нашел модули
ENV PYTHONPATH="/app"

# Запускаемый скрипт
CMD ["python", "main.py"]
