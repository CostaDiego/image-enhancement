FROM jjanzic/docker-python3-opencv

RUN apt update \
    && apt install python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-setuptools
    
RUN apt update \
    && apt upgrade

WORKDIR /usr/app/backend

COPY . .
RUN pip install --upgrade requirements/requirements.txt

EXPOSE 8123
