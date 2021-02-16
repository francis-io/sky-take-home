#!/usr/bin/env python

import random
import sys
from lotto_logic import lotto_results

input_numbers = [int(i) for i in sys.argv[1].split(",")]
# input_numbers = [1, 2, 3, 97, 98, 99]

if len(input_numbers) != 6:
    print("6 ints, example:1,2,3,4,5,6. Exiting...")
    sys.exit(1)

winning_numbers_drawn = random.sample(range(0, 61), 6)  # pseudo random
# winning_numbers_drawn = [1, 2, 3, 4, 5, 6]

# winning guesses that are also in the winning numbers drawn
winning_inputs = [num for num in input_numbers if num in winning_numbers_drawn]

print(lotto_results(winning_inputs, winning_numbers_drawn, input_numbers))
