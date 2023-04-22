from flask import request, jsonify, Blueprint
from flask_app import message_processor

lineitem_bp = Blueprint('lineitem', __name__)


@lineitem_bp.route('/lineitem', methods=['POST'])
def post_line_item():
    try:
        data = request.get_json()
        line_item = message_processor.line_item_from_json(data)
    except Exception as e:
        response = {'message': f'Failed to post due to: {str(e)}'}
        return jsonify(response), 400
    response = {'message': 'Success'}
    return jsonify(response), 201


@lineitem_bp.route('/heartbeat', methods=['GET'])
def heartbeat():
    response = {'message': 'Success'}
    return jsonify(response), 200
