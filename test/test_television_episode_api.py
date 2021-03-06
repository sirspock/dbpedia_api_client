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
from dbpedia.api.television_episode_api import TelevisionEpisodeApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTelevisionEpisodeApi(unittest.TestCase):
    """TelevisionEpisodeApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.television_episode_api.TelevisionEpisodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_televisionepisodes_get(self):
        """Test case for televisionepisodes_get

        List all instances of TelevisionEpisode  # noqa: E501
        """
        pass

    def test_televisionepisodes_id_get(self):
        """Test case for televisionepisodes_id_get

        Get a single TelevisionEpisode by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
