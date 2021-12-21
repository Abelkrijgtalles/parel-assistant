FROM python:3.11.0a3-slim-bullseye
WORKDIR /home/parel-assistant
COPY . /home/parel-assistant
RUN cd /home/parel-assistant