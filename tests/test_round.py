def test_round():

    from hangman.round import Round

    test_round = Round('python')

    assert test_round.is_word_solved() == False

def test_word_is_solved():
    from hangman.round import Round

    test_round = Round('python')
    test_round.word_status = [True for _ in test_round.word]

    assert test_round.is_word_solved() is True
