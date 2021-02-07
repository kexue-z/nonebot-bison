FROM python:3.9
RUN apt-get update && apt-get install chromium fonts-wqy-microhei
RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
RUN python3 -m pip install poetry && poetry config virtualenvs.create false
WORKDIR /app
COPY ./pyproject.toml ./poetry.lock* /app/
RUN poetry install --no-root --no-dev
COPY . /app/
CMD ["python", "bot.py"]
