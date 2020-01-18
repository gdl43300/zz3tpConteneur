FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

ADD . /usr/src/app

RUN python db.py

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
