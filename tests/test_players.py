def test_players():

    from hangman.players import HumanPlayer

    test_players = HumanPlayer(None)

    assert test_players._validate_word() == False
