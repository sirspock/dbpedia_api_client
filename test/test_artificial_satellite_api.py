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
from dbpedia.api.artificial_satellite_api import ArtificialSatelliteApi  # noqa: E501
from dbpedia.rest import ApiException


class TestArtificialSatelliteApi(unittest.TestCase):
    """ArtificialSatelliteApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.artificial_satellite_api.ArtificialSatelliteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_artificialsatellites_get(self):
        """Test case for artificialsatellites_get

        List all instances of ArtificialSatellite  # noqa: E501
        """
        pass

    def test_artificialsatellites_id_get(self):
        """Test case for artificialsatellites_id_get

        Get a single ArtificialSatellite by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()