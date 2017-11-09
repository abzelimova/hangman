def test_round():

    from hangman.round import Round

    test_round = Round('python')

    assert test_round.is_word_solved() == False

def test_word_is_solved():
    from hangman.round import Round

    test_round = Round('python')
    test_round.word_status = [True for _ in test_round.word]

    assert test_round.is_word_solved() is True

def test_draw_field(capsys):
    from hangman.round import Round
    from hangman.field import HangmanField

    test_round = Round('python')

    for i in HangmanField().states:
        test_round.draw_field()
        out, _ = capsys.readouterr()
        assert out == i or out == '\n'
        test_round.tries += 1
