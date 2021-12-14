FROM python:3.11.0a1-slim-bullseye
FROM node
WORKDIR /home/parel-assistant
COPY . /home/parel-assistant
RUN cd /home/parel-assistant
RUN cd /home/parel-assistant/website
WORKDIR /home/parel-assistant/website
RUN npm install next
RUN npm install react
RUN npm install react-dom
RUN cd ..
WORKDIR /home/parel-assistant