from lotto_logic import lotto_results


def test_lotto_results_win_all_6():
    input_numbers = [1, 2, 3, 4, 5, 6]
    winning_inputs = input_numbers
    winning_numbers_drawn = [1, 2, 3, 4, 5, 6]
    assert lotto_results(winning_inputs,
                         winning_numbers_drawn,
                         winning_inputs) == 210000


def test_lotto_results_win_3():
    input_numbers = [1, 2, 3, 97, 98, 99]
    winning_inputs = [1, 2, 3]
    winning_numbers_drawn = [1, 2, 3, 4, 5, 6]
    assert lotto_results(winning_inputs,
                         winning_numbers_drawn,
                         input_numbers) == 1620
