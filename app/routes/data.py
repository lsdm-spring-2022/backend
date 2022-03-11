from flask import Blueprint, jsonify, make_response

data = Blueprint('data', __name__)


@data.route('/api/data')
def hello_data():
    response = make_response(
        jsonify(
            {'message': 'Hello there'}
        ),
        200,
    )
    response.headers['Content-Type'] = 'application/json'
    return response
