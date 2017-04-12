#!/usr/bin/env python3

import unittest
from anagram_in_common import anagram_in_common


class TestAnagramInCommon(unittest.TestCase):

    def test_anagram_in_common(self):
        a = "abc"
        b = "ecad"

        # call method under test
        result = anagram_in_common.anagram_in_common(a, b)
        self.assertEqual(result, ('ac', 1, 2))

    def test_anagram_in_common_duplicate_letters(self):
        a = 'aabb'
        b = 'bcc'

        # call method under test
        result = anagram_in_common.anagram_in_common(a, b)
        self.assertEqual(result, ('b', 3, 2))

    def test_anagram_in_common_duplicate_letters2(self):
        a = 'aaabb'
        b = 'ccbbb'

        # call method under test
        result = anagram_in_common.anagram_in_common(a, b)
        self.assertEqual(result, ('bb', 3, 3))

    def test_anagram_in_common_duplicate_letters_all_common(self):
        a = 'bacbac'
        b = 'abcabc'

        # call method under test
        result = anagram_in_common.anagram_in_common(a, b)
        self.assertEqual(result, ('bacbac', 0, 0))

    def test_anagram_in_common_hello_billion(self):
        # example words from video
        a = 'hello'
        b = 'billion'

        # call method under test
        result = anagram_in_common.anagram_in_common(a, b)
        self.assertEqual(result, ('llo', 2, 4))
