#!/usr/bin/env python3
'''Thic has the test class to test NestedMap'''
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map



class TestAccessNestedMap(unittest.TestCase):
    """This tests the NestedMap method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
