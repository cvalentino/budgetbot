from flask import request, jsonify, Blueprint, g
from flask_app import message_processor

lineitem_bp = Blueprint('lineitem', __name__, url_prefix='/lineitem')


@lineitem_bp.route('', methods=['POST'])
def post_line_item_from_json():
    try:
        g.updated_range = message_processor.post_line_item(request.get_json())
    except Exception as e:
        response = {'message': f'Failed to post due to: {str(e)}'}
        return jsonify(response), 400
    response = {'message': 'Success'}
    return jsonify(response), 201


@lineitem_bp.after_request
def add_headers(response):
    if response.status_code == 201:
        updated_range = getattr(g, 'updated_range', None)
        if updated_range is not None:
            response.headers['Updated-Range'] = updated_range
    return response
