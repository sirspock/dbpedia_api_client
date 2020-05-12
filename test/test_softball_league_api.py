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
from dbpedia.api.softball_league_api import SoftballLeagueApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSoftballLeagueApi(unittest.TestCase):
    """SoftballLeagueApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.softball_league_api.SoftballLeagueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_softballleagues_get(self):
        """Test case for softballleagues_get

        List all instances of SoftballLeague  # noqa: E501
        """
        pass

    def test_softballleagues_id_get(self):
        """Test case for softballleagues_id_get

        Get a single SoftballLeague by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()