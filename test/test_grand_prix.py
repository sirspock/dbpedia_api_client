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
from dbpedia.models.grand_prix import GrandPrix  # noqa: E501
from dbpedia.rest import ApiException

class TestGrandPrix(unittest.TestCase):
    """GrandPrix unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GrandPrix
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.grand_prix.GrandPrix()  # noqa: E501
        if include_optional :
            return GrandPrix(
                distance = [
                    None
                    ], 
                number_of_people_attending = [
                    56
                    ], 
                end_date = [
                    '0'
                    ], 
                third_driver_country = [
                    None
                    ], 
                description = [
                    '0'
                    ], 
                first_driver_country = [
                    None
                    ], 
                fastest_driver_country = [
                    None
                    ], 
                first_driver = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                silver_medalist = [
                    None
                    ], 
                participant = [
                    '0'
                    ], 
                fastest_driver_team = [
                    None
                    ], 
                duration = [
                    1.337
                    ], 
                third_driver = [
                    None
                    ], 
                medalist = [
                    None
                    ], 
                previous_event = [
                    None
                    ], 
                champion_in_single_female = [
                    None
                    ], 
                course = [
                    None
                    ], 
                distance_laps = [
                    56
                    ], 
                champion_in_double_male = [
                    None
                    ], 
                id = '0', 
                following_event = [
                    None
                    ], 
                first_driver_team = [
                    None
                    ], 
                champion_in_single_male = [
                    None
                    ], 
                pole_driver = [
                    None
                    ], 
                second_driver_country = [
                    None
                    ], 
                bronze_medalist = [
                    None
                    ], 
                champion_in_mixed_double = [
                    None
                    ], 
                caused_by = [
                    None
                    ], 
                label = [
                    '0'
                    ], 
                gold_medalist = [
                    None
                    ], 
                second_driver = [
                    None
                    ], 
                fastest_driver = [
                    None
                    ], 
                second_team = [
                    None
                    ], 
                champion_in_single = [
                    None
                    ], 
                race_track = [
                    None
                    ], 
                third_team = [
                    None
                    ], 
                next_event = [
                    None
                    ], 
                champion_in_double_female = [
                    None
                    ], 
                champion_in_double = [
                    None
                    ], 
                start_date = [
                    '0'
                    ], 
                pole_driver_country = [
                    None
                    ], 
                champion = [
                    None
                    ], 
                pole_driver_team = [
                    None
                    ]
            )
        else :
            return GrandPrix(
        )

    def testGrandPrix(self):
        """Test GrandPrix"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
