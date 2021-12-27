FROM ubuntu:latest
FROM gcc
FROM python:3.11.0a3-slim-bullseye
WORKDIR /home/parel-assistant
COPY . /home/parel-assistant
RUN cd /home/parel-assistant
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get install patchelf
RUN apt-get install gcc -y
RUN git clone https://github.com/Nuitka/Nuitka && cd Nuitka && python3 setup.py install
RUN python3 Nuitka/bin/nuitka main.py --static-libpython=no --onefile --follow-imports --disable-ccache --show-progress --full-compat --assume-yes-for-downloads --linux-onefile-icon=/home/parel-assistant/logo/Logo64.ico --prefer-source-code
RUN rm -r -f Nuitka