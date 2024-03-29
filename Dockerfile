FROM kasmweb/core-ubuntu-bionic:1.10.0
USER root

ENV HOME /home/kasm-default-profile
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

######### Customize Container Here ###########
FROM ubuntu:latest
FROM gcc
FROM python:3.11-rc-slim
RUN apt-get -y update
RUN apt-get install git -y
RUN git clone https://github.com/Abelkrijgtalles/parel-assistant.git $HOME/Desktop/parelassistant
######### End Customizations ###########

RUN chown 1000:0 $HOME
RUN $STARTUPDIR/set_user_permission.sh $HOME

ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000