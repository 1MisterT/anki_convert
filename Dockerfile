FROM alpine:3.18.4
RUN apk add --no-cache python3 py3-pip
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
COPY src webserver
WORKDIR /webserver

ENV FLASK_DEGUB=false
ENTRYPOINT [ "python3", "-u", "main.py" ]
EXPOSE 5000