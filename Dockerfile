FROM ubuntu:20.04
RUN  apt-get update &&  apt-get install -y python3-pip && apt-get clean

#RUN  apt-get install -y python3-psycopg2
#RUN  apt-get install -y libpq-dev

WORKDIR /djangoproject

ADD . /djangoproject

RUN  pip3 install -r  requirements.txt
ENV PYTHONUNBUFFERED=1

EXPOSE 80
CMD ["gunicorn","moonsoft.wsgi:application","--bind","0.0.0.0:80"]
