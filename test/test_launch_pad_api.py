# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import dbpedia
from dbpedia.api.launch_pad_api import LaunchPadApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLaunchPadApi(unittest.TestCase):
    """LaunchPadApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.launch_pad_api.LaunchPadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_launchpads_get(self):
        """Test case for launchpads_get

        List all instances of LaunchPad  # noqa: E501
        """
        pass

    def test_launchpads_id_get(self):
        """Test case for launchpads_id_get

        Get a single LaunchPad by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()