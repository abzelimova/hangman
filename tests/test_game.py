def tsest_get_winner():
    from hangman.game import Game

    test_get_winner = Game([], [])

    assert test_get_winner.get_winner() == None
