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


class MilitaryConflict(object):
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
        'strength': 'list[str]',
        'number_of_people_attending': 'list[int]',
        'end_date': 'list[str]',
        'opponents': 'list[object]',
        'description': 'list[str]',
        'caused_by': 'list[object]',
        'label': 'list[str]',
        'type': 'list[str]',
        'casualties': 'list[int]',
        'participant': 'list[str]',
        'result': 'list[str]',
        'duration': 'list[float]',
        'previous_event': 'list[object]',
        'causalties': 'list[str]',
        'is_part_of_military_conflict': 'list[object]',
        'next_event': 'list[object]',
        'combatant': 'list[str]',
        'id': 'str',
        'following_event': 'list[object]',
        'place': 'list[object]',
        'start_date': 'list[str]'
    }

    attribute_map = {
        'strength': 'strength',
        'number_of_people_attending': 'numberOfPeopleAttending',
        'end_date': 'endDate',
        'opponents': 'opponents',
        'description': 'description',
        'caused_by': 'causedBy',
        'label': 'label',
        'type': 'type',
        'casualties': 'casualties',
        'participant': 'participant',
        'result': 'result',
        'duration': 'duration',
        'previous_event': 'previousEvent',
        'causalties': 'causalties',
        'is_part_of_military_conflict': 'isPartOfMilitaryConflict',
        'next_event': 'nextEvent',
        'combatant': 'combatant',
        'id': 'id',
        'following_event': 'followingEvent',
        'place': 'place',
        'start_date': 'startDate'
    }

    def __init__(self, strength=None, number_of_people_attending=None, end_date=None, opponents=None, description=None, caused_by=None, label=None, type=None, casualties=None, participant=None, result=None, duration=None, previous_event=None, causalties=None, is_part_of_military_conflict=None, next_event=None, combatant=None, id=None, following_event=None, place=None, start_date=None, local_vars_configuration=None):  # noqa: E501
        """MilitaryConflict - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._strength = None
        self._number_of_people_attending = None
        self._end_date = None
        self._opponents = None
        self._description = None
        self._caused_by = None
        self._label = None
        self._type = None
        self._casualties = None
        self._participant = None
        self._result = None
        self._duration = None
        self._previous_event = None
        self._causalties = None
        self._is_part_of_military_conflict = None
        self._next_event = None
        self._combatant = None
        self._id = None
        self._following_event = None
        self._place = None
        self._start_date = None
        self.discriminator = None

        self.strength = strength
        self.number_of_people_attending = number_of_people_attending
        self.end_date = end_date
        self.opponents = opponents
        self.description = description
        self.caused_by = caused_by
        self.label = label
        self.type = type
        self.casualties = casualties
        self.participant = participant
        self.result = result
        self.duration = duration
        self.previous_event = previous_event
        self.causalties = causalties
        self.is_part_of_military_conflict = is_part_of_military_conflict
        self.next_event = next_event
        self.combatant = combatant
        if id is not None:
            self.id = id
        self.following_event = following_event
        self.place = place
        self.start_date = start_date

    @property
    def strength(self):
        """Gets the strength of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The strength of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._strength

    @strength.setter
    def strength(self, strength):
        """Sets the strength of this MilitaryConflict.

        Description not available  # noqa: E501

        :param strength: The strength of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._strength = strength

    @property
    def number_of_people_attending(self):
        """Gets the number_of_people_attending of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_people_attending of this MilitaryConflict.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_people_attending

    @number_of_people_attending.setter
    def number_of_people_attending(self, number_of_people_attending):
        """Sets the number_of_people_attending of this MilitaryConflict.

        Description not available  # noqa: E501

        :param number_of_people_attending: The number_of_people_attending of this MilitaryConflict.  # noqa: E501
        :type: list[int]
        """

        self._number_of_people_attending = number_of_people_attending

    @property
    def end_date(self):
        """Gets the end_date of this MilitaryConflict.  # noqa: E501

        The end date of the event.  # noqa: E501

        :return: The end_date of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this MilitaryConflict.

        The end date of the event.  # noqa: E501

        :param end_date: The end_date of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._end_date = end_date

    @property
    def opponents(self):
        """Gets the opponents of this MilitaryConflict.  # noqa: E501

        \"opponent in a military conflict, an organisation, country, or group of countries. \"  # noqa: E501

        :return: The opponents of this MilitaryConflict.  # noqa: E501
        :rtype: list[object]
        """
        return self._opponents

    @opponents.setter
    def opponents(self, opponents):
        """Sets the opponents of this MilitaryConflict.

        \"opponent in a military conflict, an organisation, country, or group of countries. \"  # noqa: E501

        :param opponents: The opponents of this MilitaryConflict.  # noqa: E501
        :type: list[object]
        """

        self._opponents = opponents

    @property
    def description(self):
        """Gets the description of this MilitaryConflict.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MilitaryConflict.

        small description  # noqa: E501

        :param description: The description of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def caused_by(self):
        """Gets the caused_by of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The caused_by of this MilitaryConflict.  # noqa: E501
        :rtype: list[object]
        """
        return self._caused_by

    @caused_by.setter
    def caused_by(self, caused_by):
        """Sets the caused_by of this MilitaryConflict.

        Description not available  # noqa: E501

        :param caused_by: The caused_by of this MilitaryConflict.  # noqa: E501
        :type: list[object]
        """

        self._caused_by = caused_by

    @property
    def label(self):
        """Gets the label of this MilitaryConflict.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MilitaryConflict.

        short description of the resource  # noqa: E501

        :param label: The label of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this MilitaryConflict.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MilitaryConflict.

        type of the resource  # noqa: E501

        :param type: The type of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def casualties(self):
        """Gets the casualties of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The casualties of this MilitaryConflict.  # noqa: E501
        :rtype: list[int]
        """
        return self._casualties

    @casualties.setter
    def casualties(self, casualties):
        """Sets the casualties of this MilitaryConflict.

        Description not available  # noqa: E501

        :param casualties: The casualties of this MilitaryConflict.  # noqa: E501
        :type: list[int]
        """

        self._casualties = casualties

    @property
    def participant(self):
        """Gets the participant of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The participant of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this MilitaryConflict.

        Description not available  # noqa: E501

        :param participant: The participant of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._participant = participant

    @property
    def result(self):
        """Gets the result of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The result of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MilitaryConflict.

        Description not available  # noqa: E501

        :param result: The result of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._result = result

    @property
    def duration(self):
        """Gets the duration of this MilitaryConflict.  # noqa: E501

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :return: The duration of this MilitaryConflict.  # noqa: E501
        :rtype: list[float]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MilitaryConflict.

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :param duration: The duration of this MilitaryConflict.  # noqa: E501
        :type: list[float]
        """

        self._duration = duration

    @property
    def previous_event(self):
        """Gets the previous_event of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The previous_event of this MilitaryConflict.  # noqa: E501
        :rtype: list[object]
        """
        return self._previous_event

    @previous_event.setter
    def previous_event(self, previous_event):
        """Sets the previous_event of this MilitaryConflict.

        Description not available  # noqa: E501

        :param previous_event: The previous_event of this MilitaryConflict.  # noqa: E501
        :type: list[object]
        """

        self._previous_event = previous_event

    @property
    def causalties(self):
        """Gets the causalties of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The causalties of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._causalties

    @causalties.setter
    def causalties(self, causalties):
        """Sets the causalties of this MilitaryConflict.

        Description not available  # noqa: E501

        :param causalties: The causalties of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._causalties = causalties

    @property
    def is_part_of_military_conflict(self):
        """Gets the is_part_of_military_conflict of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The is_part_of_military_conflict of this MilitaryConflict.  # noqa: E501
        :rtype: list[object]
        """
        return self._is_part_of_military_conflict

    @is_part_of_military_conflict.setter
    def is_part_of_military_conflict(self, is_part_of_military_conflict):
        """Sets the is_part_of_military_conflict of this MilitaryConflict.

        Description not available  # noqa: E501

        :param is_part_of_military_conflict: The is_part_of_military_conflict of this MilitaryConflict.  # noqa: E501
        :type: list[object]
        """

        self._is_part_of_military_conflict = is_part_of_military_conflict

    @property
    def next_event(self):
        """Gets the next_event of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The next_event of this MilitaryConflict.  # noqa: E501
        :rtype: list[object]
        """
        return self._next_event

    @next_event.setter
    def next_event(self, next_event):
        """Sets the next_event of this MilitaryConflict.

        Description not available  # noqa: E501

        :param next_event: The next_event of this MilitaryConflict.  # noqa: E501
        :type: list[object]
        """

        self._next_event = next_event

    @property
    def combatant(self):
        """Gets the combatant of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The combatant of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._combatant

    @combatant.setter
    def combatant(self, combatant):
        """Sets the combatant of this MilitaryConflict.

        Description not available  # noqa: E501

        :param combatant: The combatant of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._combatant = combatant

    @property
    def id(self):
        """Gets the id of this MilitaryConflict.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this MilitaryConflict.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MilitaryConflict.

        identifier  # noqa: E501

        :param id: The id of this MilitaryConflict.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def following_event(self):
        """Gets the following_event of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The following_event of this MilitaryConflict.  # noqa: E501
        :rtype: list[object]
        """
        return self._following_event

    @following_event.setter
    def following_event(self, following_event):
        """Sets the following_event of this MilitaryConflict.

        Description not available  # noqa: E501

        :param following_event: The following_event of this MilitaryConflict.  # noqa: E501
        :type: list[object]
        """

        self._following_event = following_event

    @property
    def place(self):
        """Gets the place of this MilitaryConflict.  # noqa: E501

        Description not available  # noqa: E501

        :return: The place of this MilitaryConflict.  # noqa: E501
        :rtype: list[object]
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this MilitaryConflict.

        Description not available  # noqa: E501

        :param place: The place of this MilitaryConflict.  # noqa: E501
        :type: list[object]
        """

        self._place = place

    @property
    def start_date(self):
        """Gets the start_date of this MilitaryConflict.  # noqa: E501

        The start date of the event.  # noqa: E501

        :return: The start_date of this MilitaryConflict.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this MilitaryConflict.

        The start date of the event.  # noqa: E501

        :param start_date: The start_date of this MilitaryConflict.  # noqa: E501
        :type: list[str]
        """

        self._start_date = start_date

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
        if not isinstance(other, MilitaryConflict):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MilitaryConflict):
            return True

        return self.to_dict() != other.to_dict()
