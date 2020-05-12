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
from dbpedia.api.college_api import CollegeApi  # noqa: E501
from dbpedia.rest import ApiException


class TestCollegeApi(unittest.TestCase):
    """CollegeApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.college_api.CollegeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_colleges_get(self):
        """Test case for colleges_get

        List all instances of College  # noqa: E501
        """
        pass

    def test_colleges_id_get(self):
        """Test case for colleges_id_get

        Get a single College by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()