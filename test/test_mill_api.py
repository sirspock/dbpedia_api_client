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
from dbpedia.api.mill_api import MillApi  # noqa: E501
from dbpedia.rest import ApiException


class TestMillApi(unittest.TestCase):
    """MillApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.mill_api.MillApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mills_get(self):
        """Test case for mills_get

        List all instances of Mill  # noqa: E501
        """
        pass

    def test_mills_id_get(self):
        """Test case for mills_id_get

        Get a single Mill by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
