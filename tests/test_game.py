def test_add_round():
    from hangman.round import Round
    from hangman.game import Game
    from hangman.players import HumanPlayer

    test_game = Game()
    test_round = Round('python')
    test_player_first = HumanPlayer()
    test_player_second = HumanPlayer()

    test_game.add_round(test_round,test_player_first,test_player_second)
    assert test_game.won_rounds[test_player_second.id] == 0

def test_get_winner():
    from hangman.game import Game
    from hangman.round import Round
    from hangman.players import HumanPlayer

    test_game = Game()
    test_round = Round('python')
    test_player_first = HumanPlayer()
    test_player_second = HumanPlayer()

    test_game.add_round(test_round, test_player_first, test_player_second)
    test_game.add_round(test_round, test_player_first, test_player_second)

    assert str(test_game.get_winner()) == str(test_player_first.id)

def test_get_winner_none():
    from hangman.game import Game
    test_game = Game()

    assert test_game.get_winner() is None
