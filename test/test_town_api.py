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
from dbpedia.api.town_api import TownApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTownApi(unittest.TestCase):
    """TownApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.town_api.TownApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_towns_get(self):
        """Test case for towns_get

        List all instances of Town  # noqa: E501
        """
        pass

    def test_towns_id_get(self):
        """Test case for towns_id_get

        Get a single Town by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
