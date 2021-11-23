#!/usr/bin/env python3
'''Ths module contians classes to test client.py methods'''
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest import mock
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    '''This class tests GithubOrgClient method'''

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, url, my_mock):
        """
        Test GithubOrgClient.org
        """
        my_mock.return_value = True
        g = GithubOrgClient(url)
        self.assertEqual(g.org, True)
        my_mock.assert_called_once()
