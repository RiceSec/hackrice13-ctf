FROM alpine:3

RUN apk add --no-cache python3 py3-pip sqlite

RUN adduser --disabled-password --gecos '' hacker
RUN chown -R root:hacker /home/hacker/
RUN chmod 750 /home/hacker

COPY src /home/hacker/src
RUN chmod -R 440 /home/hacker/src

WORKDIR /home/hacker/src

RUN pip install -r requirements.txt
#RUN sqlite3 database.db < schema.sql
CMD gunicorn --bind 0.0.0.0:8000 main:app
