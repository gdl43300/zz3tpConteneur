FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

# ADD . /usr/src/app
COPY main.py /usr/src/app
COPY api.py /usr/src/app
COPY db.py /usr/src/app
COPY static /usr/src/app/static
COPY templates /usr/src/app/templates

VOLUME /usr/db

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
