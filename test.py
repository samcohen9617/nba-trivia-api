from app.api.trivia.controllers import get_most_similar_question_controller

def test_get_most_similar_question_controller():
    """Test get most similar question controller"""
    player = 'Domantas Sabonis'
    result = get_most_similar_question_controller('2023', player)
    # print(result)

test_get_most_similar_question_controller()