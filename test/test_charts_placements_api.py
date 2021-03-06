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
from dbpedia.api.charts_placements_api import ChartsPlacementsApi  # noqa: E501
from dbpedia.rest import ApiException


class TestChartsPlacementsApi(unittest.TestCase):
    """ChartsPlacementsApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.charts_placements_api.ChartsPlacementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chartsplacementss_get(self):
        """Test case for chartsplacementss_get

        List all instances of ChartsPlacements  # noqa: E501
        """
        pass

    def test_chartsplacementss_id_get(self):
        """Test case for chartsplacementss_id_get

        Get a single ChartsPlacements by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
