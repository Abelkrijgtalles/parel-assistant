FROM kasmweb/core-ubuntu-bionic:1.10.0
USER root

ENV HOME /home/kasm-default-profile
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

FROM ubuntu:latest
FROM gcc
FROM python:3.11.0a3-slim-bullseye

RUN chown 1000:0 $HOME
RUN ${STARTUPDIR}/set_user_permission.sh ${HOME}

ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p ${HOME} && chown -R 1000:0 ${HOME}
COPY . ${HOME}/parel-assistant
RUN cd ${HOME}/parel-assistant

USER 1000