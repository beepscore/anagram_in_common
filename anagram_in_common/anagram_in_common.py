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

    a_letters_remaining = list(a)
    b_letters_remaining = list(b)

    # iterate over a and b instead of over lists
    # avoid potential problem of changing list length while iterating over it
    for letter_a in a:

        if letter_a in b_letters_remaining:
            letters_in_anagram.append(letter_a)

            # to handle possible duplicate letters within one word, remove the current letter from each word
            a_letters_remaining.pop(a_letters_remaining.index(letter_a))
            b_letters_remaining.pop(b_letters_remaining.index(letter_a))
        else:
            # letter_a not in b_letters
            a_letters_remaining.pop(a_letters_remaining.index(letter_a))

    number_of_letters_removed_from_a = len(a) - len(letters_in_anagram)
    number_of_letters_removed_from_b = len(b) - len(letters_in_anagram)

    return ''.join(letters_in_anagram), number_of_letters_removed_from_a, number_of_letters_removed_from_b
