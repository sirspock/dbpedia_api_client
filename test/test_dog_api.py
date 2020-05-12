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
from dbpedia.api.dog_api import DogApi  # noqa: E501
from dbpedia.rest import ApiException


class TestDogApi(unittest.TestCase):
    """DogApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.dog_api.DogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dogs_get(self):
        """Test case for dogs_get

        List all instances of Dog  # noqa: E501
        """
        pass

    def test_dogs_id_get(self):
        """Test case for dogs_id_get

        Get a single Dog by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()