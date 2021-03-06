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
from dbpedia.api.family_api import FamilyApi  # noqa: E501
from dbpedia.rest import ApiException


class TestFamilyApi(unittest.TestCase):
    """FamilyApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.family_api.FamilyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_familys_get(self):
        """Test case for familys_get

        List all instances of Family  # noqa: E501
        """
        pass

    def test_familys_id_get(self):
        """Test case for familys_id_get

        Get a single Family by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
