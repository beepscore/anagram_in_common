#!/usr/bin/env python3


def anagram_in_common(a: str, b: str):
    """ Given two strings a and b, each contains only ascii lowercase a-z.

    Returns minimum number of letters you must remove from each a and b so that the remaining letters are anagrams.
    Assume for purposes of this puzzle, an "anagram" does not need to be a valid English word.
    It just represents a sequence of letters.
    :returns: a tuple of the form
    (anagram from a, letters removed from a, letters removed from b)
    """

    letters_in_anagram = []

    b_letters_remaining = list(b)
    """ b_letters_remaining helps handle possible duplicate letters in a. """

    # iterate over a. Note a may have duplicate letters.
    # avoid potential problem of iterating over a list while changing it
    for letter_a in a:

        # Suppose a = 'gg' and b = 'g'
        # When we get to the second letter of a, checking if it's in b is true.
        # Instead, check if the letter is in b_letters_remaining.
        if letter_a in b_letters_remaining:
            letters_in_anagram.append(letter_a)
            # Every time we 'use' a letter in b to match one in a,
            # remove the current letter from b_letters_remaining.
            b_letters_remaining.pop(b_letters_remaining.index(letter_a))

    number_of_letters_removed_from_a = len(a) - len(letters_in_anagram)
    number_of_letters_removed_from_b = len(b) - len(letters_in_anagram)

    return ''.join(letters_in_anagram), number_of_letters_removed_from_a, number_of_letters_removed_from_b
