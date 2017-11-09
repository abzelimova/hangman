def tsest_get_winner():

    from hangman.game import Game

    test_get_winner = Game(2)

    assert test_get_winner.get_winner() == int
