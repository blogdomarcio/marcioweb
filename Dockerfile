FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py collectstatic --noinput
CMD python manage.py makemigrations --noinput
CMD python manage.py migrate --noinput

COPY ./entrypoint.sh /
CMD ["sh", "/entrypoint.sh"]
