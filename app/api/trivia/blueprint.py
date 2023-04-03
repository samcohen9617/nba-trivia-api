"""
Dominion blueprint.
We create blueprint here to avoid cyclic import in __init__.py
"""

from flask import Blueprint


BP = Blueprint('trivia', __name__, url_prefix='/trivia')
