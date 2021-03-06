#!/usr/bin/env python3
'''Thic has the test class to test NestedMap'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),

    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """This tests the keyError raise in uitils.py"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''This class tests the method GetJson in the util.py module'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        '''This tests GetJson Mwthod in untils.py module'''
        class Mocked(Mock):
            '''mock class in '''

            def json(self):
                '''mocks json method'''
                return test_payload

        with patch("requests.get") as MockedClass:
            MockedClass.return_value = Mocked()
            self.assertAlmostEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''This class test Memoize method'''

    def test_memoize(self):
        '''This tests the memeoize method'''
        class TestClass:

            def a_method(self):
                '''Returns 42 which is supposed to act as returned'''
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as testClass:
            class_obj = TestClass()
            class_obj.a_property
            class_obj.a_property

            testClass.asset_called_once()
