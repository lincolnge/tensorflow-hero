FROM daocloud.io/library/ubuntu:latest
RUN apt-get update && apt-get install -y python-pip python-dev build-essential libgtk2.0-dev
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["see_hero.py"]