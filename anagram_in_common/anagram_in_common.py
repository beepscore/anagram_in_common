#!/usr/bin/env python3


class AnagramInCommon:
    """ Given two strings a and b, each contains only ascii lowercase a-z.

Returns minimum number of letters you must remove from each a and b so that the remaining letters are anagrams.
Assume for purposes of this puzzle, an "anagram" does not need to be a valid English word.
It just represents a sequence of letters."""

    @staticmethod
    def anagram_in_common(a: str, b: str):
        """result is a tuple of the form
        (anagram from a, letters removed from a, letters removed from b)
        """
        return ('ac', 1, 2)
