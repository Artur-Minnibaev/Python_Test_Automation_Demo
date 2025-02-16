# Используем Python 3.10 на Alpine Linux
FROM python:3.10-alpine3.19

# Устанавливаем зависимости для PostgreSQL и тестирования
RUN apk update && apk add --no-cache \
    postgresql-dev gcc python3-dev musl-dev libpq \
    openjdk11-jre curl tar

# Обновляем pip перед установкой зависимостей
RUN pip install --upgrade pip

RUN pip install pytest pytest-xdist

# Устанавливаем psycopg2 отдельно, чтобы избежать конфликтов
RUN pip install --no-cache-dir --timeout=100 psycopg2-binary

# Устанавливаем Allure для генерации отчетов
RUN curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz \
    && tar -zxvf allure-2.13.8.tgz -C /opt/ \
    && ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure \
    && rm allure-2.13.8.tgz

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace

# Копируем только requirements.txt (ускоряет сборку за счет кеширования)
COPY requirements.txt /usr/workspace

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект (после установки зависимостей)
COPY . /usr/workspace

# Точка входа: запуск тестов
CMD ["pytest", "-sv", "--alluredir=/usr/workspace/allure-results"]