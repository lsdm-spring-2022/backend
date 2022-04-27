FROM ubuntu:20.04

WORKDIR /app

COPY requirements.txt app.py /app/

COPY app/ /app/app/

RUN apt-get update && apt-get install -y python3-pip

RUN pip install -r requirements.txt

ENV FLASK_ENV=production

CMD ["python3", "app.py"]