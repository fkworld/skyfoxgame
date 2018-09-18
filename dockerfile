FROM python

MAINTAINER fengyong fkworld@foxmail.com

WORKDIR app
VOLUME ["/app"]
COPY Pipfile /app/
RUN python3 -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system

EXPOSE 80

CMD ["pipenv","run","python3","start.py"]