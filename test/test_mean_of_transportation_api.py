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
from dbpedia.api.mean_of_transportation_api import MeanOfTransportationApi  # noqa: E501
from dbpedia.rest import ApiException


class TestMeanOfTransportationApi(unittest.TestCase):
    """MeanOfTransportationApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.mean_of_transportation_api.MeanOfTransportationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_meanoftransportations_get(self):
        """Test case for meanoftransportations_get

        List all instances of MeanOfTransportation  # noqa: E501
        """
        pass

    def test_meanoftransportations_id_get(self):
        """Test case for meanoftransportations_id_get

        Get a single MeanOfTransportation by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()