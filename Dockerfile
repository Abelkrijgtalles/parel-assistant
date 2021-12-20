FROM python:3.11.0a1-slim-bullseye
FROM node:current-bullseye-slim
WORKDIR /home/parel-assistant
COPY . /home/parel-assistant
RUN cd /home/parel-assistant