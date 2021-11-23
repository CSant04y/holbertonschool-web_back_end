#!/usr/bin/env python3
'''Ths module contians classes to test client.py methods'''
import client
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
    @patch('client.get_json', return_value={'k': 'y'})
    def test_org(self, url_passed, my_mock):
        """
        Test GithubOrgClient.org
        """
        g = client.GithubOrgClient(url_passed)
        self.assertEqual(g.org, {'k': 'y'})
        url = 'https://api.github.com/orgs/{}'.format(url_passed)
        my_mock.assert_called_once_with(url)
