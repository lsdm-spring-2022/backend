from flask import Blueprint, jsonify, make_response, request
from app.services.data_service import get_social_media_data
from app.constants.response_codes import HTTP_BAD_REQUEST, HTTP_SERVER_ERROR
from app.utilities.request_util import validate_social_media_get_request

data = Blueprint('data', __name__)


@data.route('/api/data', methods=['GET'])
def get_data():
    args = request.args
    region = args.get('region')
    start_date = args.get('startDate')
    end_date = args.get('endDate')
    reddit = args.get('reddit')
    twitter = args.get('twitter')
    limit = args.get('limit')

    if limit is None:
        limit = 50

    missing_parameters = validate_social_media_get_request(
        region, start_date, end_date, reddit, twitter)

    if len(missing_parameters) > 0:
        response = make_response(
            jsonify(
                {
                    'message': 'Missing parameters: ' + ', '.join(missing_parameters)
                }
            ),
            HTTP_BAD_REQUEST,
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    try:
        social_media_data = get_social_media_data(
            region, start_date, end_date, reddit, twitter, limit)
        return jsonify(
            reddit=social_media_data[0],
            twitter=social_media_data[1]
        )
    except Exception as e:
        response = make_response(
            jsonify(
                {
                    'message': str(e)
                }
            ),
            HTTP_SERVER_ERROR
        )
        return response
