def test_players():

    from hangman.players import HumanPlayer

    test_players = HumanPlayer(None)

    assert test_players._validate_word() == False

def test_quess_new_word():
    from hangman.players import HumanPlayer

    value = 'Input your English word: '

    test_quess_new_word = HumanPlayer('работай')

    assert test_quess_new_word().quess_new_word() == value
