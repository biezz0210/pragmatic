FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/biezz0210/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=sggz2m$bdv1qi)+=e5v08nbomkfh_(!!&0vkpj-mn6yji)lu*%" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", 'manage.py', "runserver", "0.0.0.0:8000"]