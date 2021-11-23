#!/usr/bin/env python3
'''Ths module contians classes to test client.py methods'''
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest import mock
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """tests GithubOrgClient functionality"""
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json', return_value={'k': 'v'})
    def test_org(self, org_name, mock_gj):
        """tests that GithubOrgClient.org returns correct value"""
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org, {'k': 'v'})
        url = 'https://api.github.com/orgs/{}'.format(org_name)
        mock_gj.assert_called_once_with(url)