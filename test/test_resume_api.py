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
from dbpedia.api.resume_api import ResumeApi  # noqa: E501
from dbpedia.rest import ApiException


class TestResumeApi(unittest.TestCase):
    """ResumeApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.resume_api.ResumeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resumes_get(self):
        """Test case for resumes_get

        List all instances of Resume  # noqa: E501
        """
        pass

    def test_resumes_id_get(self):
        """Test case for resumes_id_get

        Get a single Resume by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
