FROM python:3.9

RUN apt-get update && apt-get install -y redis-server
RUN sed -i 's/bind 127.0.0.1 ::1/bind 0.0.0.0/' /etc/redis/redis.conf




RUN mkdir /app
WORKDIR /app

COPY . /app
RUN cd /app && pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
expose 5000