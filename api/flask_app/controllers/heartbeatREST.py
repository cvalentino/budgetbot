from flask import jsonify, Blueprint

heartbeat_bp = Blueprint('heartbeat', __name__)


@heartbeat_bp.route('/heartbeat', methods=['GET'])
def heartbeat():
    response = {'message': 'Success'}
    return jsonify(response), 200
