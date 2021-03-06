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
from dbpedia.api.windmill_api import WindmillApi  # noqa: E501
from dbpedia.rest import ApiException


class TestWindmillApi(unittest.TestCase):
    """WindmillApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.windmill_api.WindmillApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_windmills_get(self):
        """Test case for windmills_get

        List all instances of Windmill  # noqa: E501
        """
        pass

    def test_windmills_id_get(self):
        """Test case for windmills_id_get

        Get a single Windmill by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
