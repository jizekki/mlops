# syntax=docker/dockerfile:1

FROM python:3.7

COPY . .

ENV PATH="/.venv/bin:$PATH"

CMD ["python",  "main.py"]
