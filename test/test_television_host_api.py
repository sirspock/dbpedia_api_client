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
from dbpedia.api.television_host_api import TelevisionHostApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTelevisionHostApi(unittest.TestCase):
    """TelevisionHostApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.television_host_api.TelevisionHostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_televisionhosts_get(self):
        """Test case for televisionhosts_get

        List all instances of TelevisionHost  # noqa: E501
        """
        pass

    def test_televisionhosts_id_get(self):
        """Test case for televisionhosts_id_get

        Get a single TelevisionHost by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()