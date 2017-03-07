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
def get_probability(current, normalize=True):
    """Get probability of next strings with respect to given current one.

    :param normalize: normalize the list to have sum 1  (default: True)
    :param current:   current item                      (note that x_0 is '.')
    :return:          probability list of all possible characters
    """
    l = [float(i) for i in transitions[letter_ids[current]]]
    return [float(i) / sum(l) for i in l] if normalize else l


# Test if the function is true, check with given example
assert str(get_probability('q', False)[letter_ids['u']]) == '0.9949749'


def sample_random_string(n):
    """For a given n, write a program to sample random strings with letters.

    x_1, x_2, ..., x_n from get_probability(x_{1:N}|x_0)

    :param n: length of sample string
    :return:  sample random string
    """
    current_char, random_string = '.', ''
    for i in xrange(n):
        probabilities = get_probability(current_char)
        current_char = np.random.choice(
            alphabet, p=probabilities)
        random_string += current_char
    return random_string


for i in np.random.randint(low=1, high=10, size=10):
    print('length: {}, text: {}'.format(i, sample_random_string(i)))


def string_guess(string):
    """Guess the original string.

    :param string: string with missing letters
    :return:       full string
    """
    missing_indices = [pos for pos, char in enumerate(string) if char == '_']
    string = list(string)
    for i in missing_indices:
        prev_char = string[i-1] if i > 0 else '.'
        probabilities = get_probability(prev_char)
        string[i] = np.random.choice(
            alphabet, p=probabilities)
    return ''.join(string)


def display_string_guess(l_params, times):
    """Display the guess string in meaningful way.

    :param l_params: list of params you want to test (string list)
    :param times:    how many times you want to test (integer)
    """
    for param in l_params:
        for t in range(1, times+1):
            print('"{}" string, try number {:>2}: "{}"'.format(
                param, t, string_guess(param)))


display_string_guess(['t__.'], 10)
