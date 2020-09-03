FROM jjanzic/docker-python3-opencv

RUN apt update \
    && apt upgrade

WORKDIR /usr/app/backend

COPY . .
RUN pip install --upgrade requirements/requirements.txt

EXPOSE 8123
