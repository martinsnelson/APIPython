# FROM python:3.7.2
FROM python:3.7.2-stretch

# seta o diretorio de trabalho para /app 
WORKDIR /app

# Copia o contedo do diretorio altual para /app
ADD . /app

# instala as dependencias
RUN pip install -r requirements.txt

# roda o comando para start uWSGI
CMD ["uwsgi", "app.ini"]