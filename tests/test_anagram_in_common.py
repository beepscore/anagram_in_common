#!/usr/bin/env python3

import unittest
from anagram_in_common import anagram_in_common

class TestAnagramInCommon(unittest.TestCase):

    def test_anagram_in_common(self):
        a = "abc"
        b = "ecad"

        # call method under test
        result = anagram_in_common.AnagramInCommon.anagram_in_common(a, b)
        # result is a tuple of the form
        # (anagram from a, letters removed from a, letters removed from b)
        self.assertEqual(result, ('ac', 1, 2))

