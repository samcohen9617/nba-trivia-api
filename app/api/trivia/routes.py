"""Dominion routes"""
from flask import request
from .blueprint import BP
from .controllers import get_nickname_question_controller, get_most_similar_question_controller

@BP.route('/nickname', methods=['GET'])
def get_nickname_question():
    """Get nickname question route"""
    return get_nickname_question_controller()

@BP.route('/most-similar', methods=['GET'])
def get_most_similar_question():
    """Get most similar question route"""
    player = request.args.get('playerName', None).replace('-', ' ')
    return get_most_similar_question_controller('2023', player)