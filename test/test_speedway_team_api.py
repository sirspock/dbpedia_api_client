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
from dbpedia.api.speedway_team_api import SpeedwayTeamApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSpeedwayTeamApi(unittest.TestCase):
    """SpeedwayTeamApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.speedway_team_api.SpeedwayTeamApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_speedwayteams_get(self):
        """Test case for speedwayteams_get

        List all instances of SpeedwayTeam  # noqa: E501
        """
        pass

    def test_speedwayteams_id_get(self):
        """Test case for speedwayteams_id_get

        Get a single SpeedwayTeam by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()