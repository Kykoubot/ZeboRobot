FROM debian:11
FROM python:3.9.9-slim-buster

WORKDIR /ZeboRobot/

RUN apt update && apt upgrade -y
RUN apt-get --no-install-recommends -y install git

RUN apt-get install --no-install-recommends -y wget python3-pip curl bash neofetch ffmpeg software-properties-common



COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3", "-m", "ZeboRobot"]
