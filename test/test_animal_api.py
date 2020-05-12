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
from dbpedia.api.animal_api import AnimalApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAnimalApi(unittest.TestCase):
    """AnimalApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.animal_api.AnimalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_animals_get(self):
        """Test case for animals_get

        List all instances of Animal  # noqa: E501
        """
        pass

    def test_animals_id_get(self):
        """Test case for animals_id_get

        Get a single Animal by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()