#!/usr/bin/env python3
'''Ths module contians classes to test client.py methods'''
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import Response


class TestGithubOrgClient(unittest.TestCase):
    '''This class tests GithubOrgClient method'''

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={'k': 'y'})
    def test_org(self, url, my_mock):
        """
        Test GithubOrgClient.org
        """
        my_mock.return_value = True
        g = client.GithubOrgClient(url)
        self.assertEqual(g.org, True)
        my_mock.assert_called_once()

    @parameterized.expand([
        ('random-url', {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        '''This tests _puclic_repo'''
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            respsonse = client.GithubOrgClient(name)._public_repos_url
            self.assertEqual(respsonse, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        '''This tests public_repo'''
        payload = [{'name': 'Google'}, {'name': 'TT'}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mockedProperty:
            mockedProperty.return_value = 'hello'
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ['Google', 'TT'])

            mockedProperty.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expectation):
        '''self descriptive'''
        self.assertEqual(GithubOrgClient.has_license(repo, key), expectation)
