## mssql-python-pyodbc
## Python runtime with pyodbc to connect to SQL Server
FROM ubuntu:16.04
#
## apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5\
    && rm -rf /var/lib/apt/lists/*
#
## adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
#
## install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17=17.3.1.1-1 unixodbc-dev
#
## install SQL Server tools
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools=17.3.0.1-1
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"
#
RUN apt-get update \
&& apt-get install -y python3-pip python3-dev \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip
#
## install necessary locales
RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen
#
## install additional utilities
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini
RUN export PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1
RUN apt-get update && apt-get install -y unixodbc freetds-dev freetds-bin tdsodbc
#RUN apt-get install freetds-dev freetds-bin tdsodbc -y
##RUN sudo dpkg-reconfigure tdsodbc -y
RUN apt-get update && apt-get install gettext nano vim -y
#
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt

## add sample code
RUN mkdir /src
ADD . /src
WORKDIR /src