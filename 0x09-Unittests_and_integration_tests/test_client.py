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
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        ''' self descriptive '''
        mock.return_value = True
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        self.assertEqual(spec.org, True)
        mock.assert_called_once_with(endpoint)
