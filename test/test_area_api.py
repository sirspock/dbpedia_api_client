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
from dbpedia.api.area_api import AreaApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAreaApi(unittest.TestCase):
    """AreaApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.area_api.AreaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_areas_get(self):
        """Test case for areas_get

        List all instances of Area  # noqa: E501
        """
        pass

    def test_areas_id_get(self):
        """Test case for areas_id_get

        Get a single Area by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()