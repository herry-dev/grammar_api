from flask import Blueprint, request, jsonify

charbp = Blueprint('character', __name__, url_prefix='/char')

@charbp.route('/<char>', methods=['GET'])
def get_player(char):
    return jsonify({"name":char})