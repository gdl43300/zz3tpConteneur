from flask import Flask, request, render_template
from api import api

app = Flask(__name__)
app.register_blueprint(api)


@app.route('/')
def hello_world():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
