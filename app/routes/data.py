from flask import Blueprint, jsonify, make_response, request
from app.services.data_service import get_social_media_data
from app.constants.response_codes import HTTP_OK

data = Blueprint('data', __name__)


@data.route('/api/data', methods=['GET'])
def hello_data():
    args = request.args
    # TODO Validate use input
    country = args.get('country')
    date = args.get('date')
    source = args.get('source')

    data = get_social_media_data(country, date, source)
    response = make_response(
        jsonify(
            data
        ),
        HTTP_OK,
    )
    response.headers['Content-Type'] = 'application/json'
    return response
