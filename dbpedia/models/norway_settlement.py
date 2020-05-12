# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dbpedia.configuration import Configuration


class NorwaySettlement(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'most_down_point': 'list[object]',
        'landskap': 'list[str]',
        'center': 'list[str]',
        'description': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'most_down_point': 'mostDownPoint',
        'landskap': 'landskap',
        'center': 'center',
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, most_down_point=None, landskap=None, center=None, description=None, id=None, label=None, type=None, local_vars_configuration=None):  # noqa: E501
        """NorwaySettlement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._most_down_point = None
        self._landskap = None
        self._center = None
        self._description = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.most_down_point = most_down_point
        self.landskap = landskap
        self.center = center
        self.description = description
        if id is not None:
            self.id = id
        self.label = label
        self.type = type

    @property
    def most_down_point(self):
        """Gets the most_down_point of this NorwaySettlement.  # noqa: E501

        Description not available  # noqa: E501

        :return: The most_down_point of this NorwaySettlement.  # noqa: E501
        :rtype: list[object]
        """
        return self._most_down_point

    @most_down_point.setter
    def most_down_point(self, most_down_point):
        """Sets the most_down_point of this NorwaySettlement.

        Description not available  # noqa: E501

        :param most_down_point: The most_down_point of this NorwaySettlement.  # noqa: E501
        :type: list[object]
        """

        self._most_down_point = most_down_point

    @property
    def landskap(self):
        """Gets the landskap of this NorwaySettlement.  # noqa: E501

        Description not available  # noqa: E501

        :return: The landskap of this NorwaySettlement.  # noqa: E501
        :rtype: list[str]
        """
        return self._landskap

    @landskap.setter
    def landskap(self, landskap):
        """Sets the landskap of this NorwaySettlement.

        Description not available  # noqa: E501

        :param landskap: The landskap of this NorwaySettlement.  # noqa: E501
        :type: list[str]
        """

        self._landskap = landskap

    @property
    def center(self):
        """Gets the center of this NorwaySettlement.  # noqa: E501

        Description not available  # noqa: E501

        :return: The center of this NorwaySettlement.  # noqa: E501
        :rtype: list[str]
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this NorwaySettlement.

        Description not available  # noqa: E501

        :param center: The center of this NorwaySettlement.  # noqa: E501
        :type: list[str]
        """

        self._center = center

    @property
    def description(self):
        """Gets the description of this NorwaySettlement.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this NorwaySettlement.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NorwaySettlement.

        small description  # noqa: E501

        :param description: The description of this NorwaySettlement.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this NorwaySettlement.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this NorwaySettlement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NorwaySettlement.

        identifier  # noqa: E501

        :param id: The id of this NorwaySettlement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this NorwaySettlement.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this NorwaySettlement.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this NorwaySettlement.

        short description of the resource  # noqa: E501

        :param label: The label of this NorwaySettlement.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this NorwaySettlement.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this NorwaySettlement.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NorwaySettlement.

        type of the resource  # noqa: E501

        :param type: The type of this NorwaySettlement.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NorwaySettlement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NorwaySettlement):
            return True

        return self.to_dict() != other.to_dict()