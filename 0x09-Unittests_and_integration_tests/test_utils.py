#!/usr/bin/python3
'''Thic has the test class to test NestedMap'''
import unittest
from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class
from typing import Mapping, Sequence, Any
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """This tests the NestedMap method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_nested_map(self, nested_map: Mapping, path: Sequence, expected):
        """test nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
