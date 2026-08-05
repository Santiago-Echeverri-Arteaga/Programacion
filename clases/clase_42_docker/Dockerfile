FROM python:3.12-slim

WORKDIR /curso
COPY demo.py .

RUN useradd --create-home estudiante
USER estudiante

CMD ["python", "demo.py"]
