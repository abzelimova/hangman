def test_is_finished():
    from hangman.round import Round
    test_round = Round('python')

    assert test_round.is_finished() is False

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

def test_draw_result_right(capsys):
    from hangman.round import Round
    test_round = Round('no')



    test_round.try_letter('n')
    test_round.try_letter('o')

    test_round.draw_result()
    out, _ = capsys.readouterr()
    assert out == '\n----------\nWord is solved, a point goes to you!\n'
