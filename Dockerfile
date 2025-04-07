FROM python:3.12

RUN pip install uv

WORKDIR /code

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

CMD ["uv", "run", "run.py"]