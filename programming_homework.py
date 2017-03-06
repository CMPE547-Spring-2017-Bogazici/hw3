"""In this exercise we model a string of text using a Markov(1) model.

For simplicity we only consider letters 'a-z'. Capital letters 'A-Z'
are mapped to the corresponding ones.
All remaining letters, symbols, numbers, including spaces, are denoted by '.'.
"""

import csv
import numpy as np

alphabet = [chr(i + ord('a')) for i in range(26)]
alphabet.append('.')
letter_ids = {c: i for i, c in enumerate(alphabet)}

with open('transitions.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    transitions = [row for row in reader]


# Note: np.random.choice ValueError: probabilities do not sum to 1
def get_probality(current, normalize=True):
    """Get probality of next strings with respect to given current one.

    :param normalize: normalize the list to have sum 1  (default: True)
    :param current: current item                        (note that x_0 is '.')
    :return: probality list of all possible characters
    """
    l = [float(i) for i in transitions[letter_ids[current]]]
    return [float(i) / sum(l) for i in l] if normalize else l


# Test if the function is true, check with given example
assert str(get_probality('q', False)[letter_ids['u']]) == '0.9949749'


def sample_random_string(n):
    """For a given n, write a program to sample random strings with letters.

    x_1, x_2, ..., x_n from get_probality(x_{1:N}|x_0)

    :param n: length of sample string
    :return:  sample random string
    """
    current_char, random_string = '.', ''
    for i in xrange(10):
        random_string += current_char
        probabilities = get_probality(current_char)
        current_char = np.random.choice(
            alphabet, p=probabilities)
    return random_string


print(sample_random_string(10))
