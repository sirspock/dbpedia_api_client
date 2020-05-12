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
from dbpedia.api.host_api import HostApi  # noqa: E501
from dbpedia.rest import ApiException


class TestHostApi(unittest.TestCase):
    """HostApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.host_api.HostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_hosts_get(self):
        """Test case for hosts_get

        List all instances of Host  # noqa: E501
        """
        pass

    def test_hosts_id_get(self):
        """Test case for hosts_id_get

        Get a single Host by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()