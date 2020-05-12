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
from dbpedia.api.geological_period_api import GeologicalPeriodApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGeologicalPeriodApi(unittest.TestCase):
    """GeologicalPeriodApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.geological_period_api.GeologicalPeriodApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_geologicalperiods_get(self):
        """Test case for geologicalperiods_get

        List all instances of GeologicalPeriod  # noqa: E501
        """
        pass

    def test_geologicalperiods_id_get(self):
        """Test case for geologicalperiods_id_get

        Get a single GeologicalPeriod by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()