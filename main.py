from flask import Flask, request, render_template, json
from api import api
from db import insert_into_db

app = Flask(__name__)
app.register_blueprint(api)


@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        data = request.data.decode("utf-8").split(",")
        insert_into_db(data[0], data[1])
    return render_template('login.html')


@app.route('/table')
def table():
    return render_template('table.html')


if __name__ == '__main__':
    app.run(debug=True)
