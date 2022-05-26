FROM python:3.9.7-slim-buster

RUN apt update && apt-get upgrade -y

RUN apt install git curl python3-pip ffmpeg -y
RUN python3 -m pip install --upgrade pip

COPY . .

RUN python3 -m pip install -U -r requirements.txt

CMD ["python3", "-m", "ZeboRobot"]
