from flask import jsonify, Blueprint

heartbeat_bp = Blueprint('heartbeat', __name__, url_prefix='/heartbeat')


@heartbeat_bp.route('', methods=['GET'])
def heartbeat():
    response = {'message': 'Success'}
    return jsonify(response), 200
