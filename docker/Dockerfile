FROM alpine:3.6
ENV PYTHONUNBUFFERED 1

RUN echo 'http://mirrors.aliyun.com/alpine/v3.6/main/' > /etc/apk/repositories
RUN echo 'http://mirrors.aliyun.com/alpine/v3.6/community/' >> /etc/apk/repositories

RUN mkdir /app
RUN apk update
RUN apk add python3 py3-greenlet py3-zmq py3-gevent


COPY ./requirements.txt /app/
COPY ./server1.py /app/
COPY ./server0.py /app/

RUN pip3 install -r /app/requirements.txt
RUN pip3 install --upgrade cardbin
RUN rm -rf /app/requirements.txt
RUN chmod +x /app/*.py

WORKDIR /app

# ENTRYPOINT ["/entrypoint.sh"]
