# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dbpedia
from dbpedia.models.drug import Drug  # noqa: E501
from dbpedia.rest import ApiException

class TestDrug(unittest.TestCase):
    """Drug unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Drug
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.drug.Drug()  # noqa: E501
        if include_optional :
            return Drug(
                iupac_name = [
                    '0'
                    ], 
                ch_ebi = [
                    '0'
                    ], 
                bioavailability = [
                    1.337
                    ], 
                description = [
                    '0'
                    ], 
                id = '0', 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                melting_point = [
                    None
                    ], 
                boiling_point = [
                    None
                    ]
            )
        else :
            return Drug(
        )

    def testDrug(self):
        """Test Drug"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()