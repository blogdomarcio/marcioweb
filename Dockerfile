FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /
CMD ["sh", "/entrypoint.sh"]
