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
from dbpedia.api.ligament_api import LigamentApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLigamentApi(unittest.TestCase):
    """LigamentApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.ligament_api.LigamentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ligaments_get(self):
        """Test case for ligaments_get

        List all instances of Ligament  # noqa: E501
        """
        pass

    def test_ligaments_id_get(self):
        """Test case for ligaments_id_get

        Get a single Ligament by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()