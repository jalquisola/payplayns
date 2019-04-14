FROM jenkins:latest
USER root
RUN apt-get update
RUN apt-get install python3 python3-pip
