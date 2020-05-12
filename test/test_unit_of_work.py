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
from dbpedia.models.unit_of_work import UnitOfWork  # noqa: E501
from dbpedia.rest import ApiException

class TestUnitOfWork(unittest.TestCase):
    """UnitOfWork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UnitOfWork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.unit_of_work.UnitOfWork()  # noqa: E501
        if include_optional :
            return UnitOfWork(
                description = [
                    '0'
                    ], 
                developer = [
                    None
                    ], 
                id = '0', 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ]
            )
        else :
            return UnitOfWork(
        )

    def testUnitOfWork(self):
        """Test UnitOfWork"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()