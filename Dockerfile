FROM python:2.7

MAINTAINER Dmitry Korobitsin <korobicin@gmail.com>

ENV SIMULATOR_VERSION 0.5.1

COPY . /tmp/simulator/

RUN set -x \
    && pip install /tmp/simulator \
    && mv /tmp/simulator/cisco_2801.conf / \
    && rm -rf /tmp/simulator

EXPOSE 161

CMD ["simulator", "-s", "--host", "0.0.0.0", "--port", "161", "--walk_file", "cisco_2801.conf"]
