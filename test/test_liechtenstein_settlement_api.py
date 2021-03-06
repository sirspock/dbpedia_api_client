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
from dbpedia.api.liechtenstein_settlement_api import LiechtensteinSettlementApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLiechtensteinSettlementApi(unittest.TestCase):
    """LiechtensteinSettlementApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.liechtenstein_settlement_api.LiechtensteinSettlementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_liechtensteinsettlements_get(self):
        """Test case for liechtensteinsettlements_get

        List all instances of LiechtensteinSettlement  # noqa: E501
        """
        pass

    def test_liechtensteinsettlements_id_get(self):
        """Test case for liechtensteinsettlements_id_get

        Get a single LiechtensteinSettlement by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
