FROM python:3.8-slim
EXPOSE 5000
RUN apt-get update && apt-get install -y xinetd
COPY prysoner.xinetd /etc/xinetd.d/prysoner

WORKDIR /app
COPY main.py flag.txt ./

CMD [ "xinetd", "-dontfork" ]