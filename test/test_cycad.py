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
from dbpedia.models.cycad import Cycad  # noqa: E501
from dbpedia.rest import ApiException

class TestCycad(unittest.TestCase):
    """Cycad unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Cycad
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.cycad.Cycad()  # noqa: E501
        if include_optional :
            return Cycad(
                classis = [
                    None
                    ], 
                sub_family = [
                    None
                    ], 
                scientific_name = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                binomial_authority = [
                    None
                    ], 
                cultivated_variety = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                sub_tribus = [
                    None
                    ], 
                sub_classis = [
                    None
                    ], 
                taxon = [
                    None
                    ], 
                id = '0', 
                tribus = [
                    None
                    ], 
                order = [
                    None
                    ], 
                conservation_status = [
                    '0'
                    ], 
                super_family = [
                    None
                    ], 
                binomial = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                conservation_status_system = [
                    '0'
                    ], 
                kingdom = [
                    None
                    ], 
                hybrid = [
                    None
                    ], 
                phylum = [
                    None
                    ], 
                species = [
                    None
                    ], 
                genus = [
                    None
                    ], 
                domain = [
                    None
                    ], 
                super_tribus = [
                    None
                    ], 
                family = [
                    None
                    ]
            )
        else :
            return Cycad(
        )

    def testCycad(self):
        """Test Cycad"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()