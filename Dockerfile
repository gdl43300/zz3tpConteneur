FROM python:3

<<<<<<< HEAD


# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "db.py" ]
=======
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

ADD . /usr/src/app

RUN python db.py

ENTRYPOINT [ "python" ]
>>>>>>> add dockerfile and requirements

CMD [ "main.py" ]
