FROM python:slim
EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update && apt install -y python3-dev gcc libc-dev
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]