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
from dbpedia.api.road_tunnel_api import RoadTunnelApi  # noqa: E501
from dbpedia.rest import ApiException


class TestRoadTunnelApi(unittest.TestCase):
    """RoadTunnelApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.road_tunnel_api.RoadTunnelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_roadtunnels_get(self):
        """Test case for roadtunnels_get

        List all instances of RoadTunnel  # noqa: E501
        """
        pass

    def test_roadtunnels_id_get(self):
        """Test case for roadtunnels_id_get

        Get a single RoadTunnel by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
