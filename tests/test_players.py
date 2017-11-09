def test_players():

    from hangman.players import HumanPlayer

    test_players = HumanPlayer(None)

    assert test_players._validate_word() == False

def test_quess_new_word():
    from hangman.players import ComputerPlayer
    from hangman.players import HumanPlayer

    value = 'Input your English word: '
    test_ai = ComputerPlayer

    assert len(test_ai.quess_new_word()) > 0

    test_quess_new_word = HumanPlayer('работай')

    assert test_quess_new_word().quess_new_word() == value

def test_select_other_player():
    from hangman.players import HumanPlayer
    value = 'ai'
    test_select_other_player = HumanPlayer('ai')
    assert  test_select_other_player.select_other_player() == value

