from flask import request, jsonify, Blueprint, g
from flask_app import message_processor, sheet_service

lineitem_bp = Blueprint('lineitem', __name__)


@lineitem_bp.route('/lineitem', methods=['POST'])
def post_line_item():
    try:
        data = request.get_json()
        line_item = message_processor.line_item_from_json(data)
        sheet_response = sheet_service.appendLineItem(line_item)
        g.updated_range = sheet_response.updates.updatedRange
    except Exception as e:
        response = {'message': f'Failed to post due to: {str(e)}'}
        return jsonify(response), 400
    response = {'message': 'Success'}
    return jsonify(response), 201


@lineitem_bp.after_request
def add_headers(response):
    updated_range = getattr(g, 'updated_range')
    if updated_range is not None:
        response.headers['Updated-Range'] = updated_range
    return response
