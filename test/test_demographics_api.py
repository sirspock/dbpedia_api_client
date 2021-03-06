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
from dbpedia.api.demographics_api import DemographicsApi  # noqa: E501
from dbpedia.rest import ApiException


class TestDemographicsApi(unittest.TestCase):
    """DemographicsApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.demographics_api.DemographicsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_demographicss_get(self):
        """Test case for demographicss_get

        List all instances of Demographics  # noqa: E501
        """
        pass

    def test_demographicss_id_get(self):
        """Test case for demographicss_id_get

        Get a single Demographics by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
