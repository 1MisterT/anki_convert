FROM python:3.9
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
COPY src webserver
WORKDIR /webserver

ENV FLASK_DEGUB=false
ENTRYPOINT [ "python3", "-u", "main.py" ]
EXPOSE 5000