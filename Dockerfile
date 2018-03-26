FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapp
WORKDIR /webapp
ADD requirements.txt /webapp/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /webapp/
# RUN ./run_migrations.sh
