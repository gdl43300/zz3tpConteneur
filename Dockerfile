FROM python:3



# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "db.py" ]

CMD [ "main.py" ]
