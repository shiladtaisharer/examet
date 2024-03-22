from random import shuffle
from copy import copy
numbers = [1, 2, 3, 4, 5]
shuffled_numbers = copy(numbers)
shuffle(shuffled_numbers)
print(numbers)
print(shuffled_numbers)
