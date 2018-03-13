from game import game

def test_game_01():
    assert game ('R','S') == 'p1', 'Unexpected result'
    assert game ('S','R') == 'p2', 'Unexpected result'
    assert game ('S','P') == 'p1', 'Unexpected result'
    assert game ('S','S') == 'Empate', 'Unexpected result'
    assert game ('r','s') == 'p1', 'Unexpected result'
    assert game ('n','i') == 'False', 'Unexpected result'
    




