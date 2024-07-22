FROM python:latest

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]