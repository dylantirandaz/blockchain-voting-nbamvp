from flask import Blueprint, request, jsonify
from app import blockchain
from .database import add_vote, get_votes

bp = Blueprint('routes', __name__)

@bp.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    candidate = data['candidate']
    add_vote(candidate)
    new_block = blockchain.Block(len(blockchain.chain), time.time(), get_votes(), blockchain.chain[-1].hash)
    blockchain.add_block(new_block)
    return "Vote added successfully"

@bp.route('/results', methods=['GET'])
def results():
    return jsonify(get_votes())
