def test_players():

    from hangman.players import HumanPlayer

    test_players = HumanPlayer()

    assert test_players._validate_word('') == False

def test_quess_new_word():
    from hangman.players import HumanPlayer

    value = 'Input your English word: '

    test_quess_ru_word = HumanPlayer('работай')
    test_quess_word = HumanPlayer('')
    test_quess_new_word = HumanPlayer('python')

    assert test_quess_ru_word().quess_new_word() == value
    assert test_quess_word().quess_new_word() == False
    assert test_quess_new_word().quess_new_word() == True

def test_comp_quess_new_word():
    from hangman.players import ComputerPlayer
    test_ai = ComputerPlayer()

    assert len(test_ai.quess_new_word()) > 0

def test_select_other_player():
    from hangman.players import HumanPlayer
    value = 'ai'
    test_select_other_player = HumanPlayer(value)
    assert  test_select_other_player.select_other_player() == value

def test_comp_should_change_turns():
    from hangman.players import ComputerPlayer
    test_ai = ComputerPlayer()

    assert test_ai.should_change_turns() is False


