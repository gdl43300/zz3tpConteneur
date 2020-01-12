from flask import jsonify, Blueprint
from db import get_all_from_db

api = Blueprint("api", __name__)


@api.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': get_all_from_db()})
