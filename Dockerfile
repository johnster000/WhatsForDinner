## Python runtime
FROM ubuntu:20.04
#
## install python and pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt-get install -y python3.10 python3.10-dev
RUN apt-get install -y python3-pip
#
## install necessary locales
RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen
#
## install additional utilities
RUN apt-get update && apt-get install gettext nano vim -y
#
## install requirements
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt
#
## add code to src folder
RUN mkdir /src
ADD . /src
WORKDIR /src