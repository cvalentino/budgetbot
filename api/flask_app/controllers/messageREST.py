from flask import request, jsonify, Blueprint
from flask_app import message_processor

message_bp = Blueprint('message', __name__, url_prefix='/message')


@message_bp.route('', methods=['POST'])
def handle_message():
    try:
        response_message = message_processor.consume_message(request.get_json())
    except Exception as e:
        response = {'message': f'Request failed due to: {str(e)}'}
        return jsonify(response), 400
    response = response_message
    return jsonify(response), 200

