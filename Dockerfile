FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /blog
COPY . /blog/
WORKDIR /blog

COPY ./requirements.txt usr/src/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]