FROM python:3.11.0a1-slim-bullseye
RUN cd ~
RUN echo from parelassistant import ding\n\nding.main() > start.py
RUN python3 start.py