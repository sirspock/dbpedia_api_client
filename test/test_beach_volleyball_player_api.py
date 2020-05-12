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
from dbpedia.api.beach_volleyball_player_api import BeachVolleyballPlayerApi  # noqa: E501
from dbpedia.rest import ApiException


class TestBeachVolleyballPlayerApi(unittest.TestCase):
    """BeachVolleyballPlayerApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.beach_volleyball_player_api.BeachVolleyballPlayerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_beachvolleyballplayers_get(self):
        """Test case for beachvolleyballplayers_get

        List all instances of BeachVolleyballPlayer  # noqa: E501
        """
        pass

    def test_beachvolleyballplayers_id_get(self):
        """Test case for beachvolleyballplayers_id_get

        Get a single BeachVolleyballPlayer by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()