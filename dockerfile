FROM python

MAINTAINER fengyong fkworld@foxmail.com

WORKDIR app
VOLUME ["/app"]
COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN python3 -m pip install --upgrade pip -i https://pypi.douban.com/simple
RUN pip install pipenv -i https://pypi.douban.com/simple
RUN pipenv install

EXPOSE 80

CMD ["pipenv","run","python3","start.py"]