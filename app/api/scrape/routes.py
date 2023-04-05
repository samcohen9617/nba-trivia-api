"""Dominion routes"""
from .blueprint import BP
from .controllers import scrape_data_controller

@BP.route('/scrape_data', methods=['GET'])
def scrape_data():
    """Get nickname question route"""
    return scrape_data_controller()
