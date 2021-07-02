# docker build . -t ctfkomatik-pwn1
# docker run --rm -it -p 0.0.0.0:22221:5000 --name ctfkomatik-pwn1 ctfkomatik-pwn1
FROM ubuntu:20.04
EXPOSE 5000
RUN apt-get update
RUN apt-get install socat wget gcc make -y
RUN mkdir /app
WORKDIR /app
COPY flag.txt /app/flag.txt
COPY chal /app/chal
RUN chown root:root flag.txt
RUN chmod 755 chal
RUN chmod 444 flag.txt
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /bin/dash /bin/sh /bin/cat /usr/bin/id /bin/ls
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./chal,su=nobody