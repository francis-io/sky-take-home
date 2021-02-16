#!/usr/bin/env python

import math


def three_to_five_winners(winning_inputs, winning_numbers_drawn):
    flat_winnings = len(winning_inputs * 500)

    variable_winnings = [item for item in winning_numbers_drawn
                         if item not in winning_inputs]

    return math.prod(variable_winnings) + flat_winnings


def lotto_results(winning_inputs, winning_numbers_drawn, input_numbers):
    if len(winning_inputs) == 6:
        return(sum(winning_inputs * 10000))

    elif len(winning_inputs) > 2 and len(winning_inputs) < 6:
        return(three_to_five_winners(winning_inputs, winning_numbers_drawn))

    elif len(winning_inputs) < 3:  # everyone wins right?
        return(sum(input_numbers))
