FROM python:3.8-alpine
WORKDIR /app
RUN apk add g++ freetds-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["/usr/local/bin/python", "main.py"]