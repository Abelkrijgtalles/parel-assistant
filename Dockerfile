FROM python:3.11.0a1-slim-bullseye
RUN apt-get install make
RUN make run