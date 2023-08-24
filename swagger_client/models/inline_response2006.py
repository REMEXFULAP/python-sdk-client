# coding: utf-8

"""
    REMESITA API REST

    Api de remesita.com para desarrolladores. Primero obten tu apiKey y apiSecret, y para autenticarte debes ejecutar el endpoint rest/v1/auth en la respuesta obtendrás un token de acceso que debes usar en el resto de peticiones  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class InlineResponse2006(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pg': 'int',
        'pg_size': 'int',
        'pages': 'int',
        'total': 'int',
        'allow_next': 'bool',
        'items': 'list[InlineResponse2006Items]'
    }

    attribute_map = {
        'pg': 'pg',
        'pg_size': 'pgSize',
        'pages': 'pages',
        'total': 'total',
        'allow_next': 'allowNext',
        'items': 'items'
    }

    def __init__(self, pg=None, pg_size=None, pages=None, total=None, allow_next=None, items=None, _configuration=None):  # noqa: E501
        """InlineResponse2006 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pg = None
        self._pg_size = None
        self._pages = None
        self._total = None
        self._allow_next = None
        self._items = None
        self.discriminator = None

        if pg is not None:
            self.pg = pg
        if pg_size is not None:
            self.pg_size = pg_size
        if pages is not None:
            self.pages = pages
        if total is not None:
            self.total = total
        if allow_next is not None:
            self.allow_next = allow_next
        if items is not None:
            self.items = items

    @property
    def pg(self):
        """Gets the pg of this InlineResponse2006.  # noqa: E501


        :return: The pg of this InlineResponse2006.  # noqa: E501
        :rtype: int
        """
        return self._pg

    @pg.setter
    def pg(self, pg):
        """Sets the pg of this InlineResponse2006.


        :param pg: The pg of this InlineResponse2006.  # noqa: E501
        :type: int
        """

        self._pg = pg

    @property
    def pg_size(self):
        """Gets the pg_size of this InlineResponse2006.  # noqa: E501


        :return: The pg_size of this InlineResponse2006.  # noqa: E501
        :rtype: int
        """
        return self._pg_size

    @pg_size.setter
    def pg_size(self, pg_size):
        """Sets the pg_size of this InlineResponse2006.


        :param pg_size: The pg_size of this InlineResponse2006.  # noqa: E501
        :type: int
        """

        self._pg_size = pg_size

    @property
    def pages(self):
        """Gets the pages of this InlineResponse2006.  # noqa: E501


        :return: The pages of this InlineResponse2006.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this InlineResponse2006.


        :param pages: The pages of this InlineResponse2006.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def total(self):
        """Gets the total of this InlineResponse2006.  # noqa: E501


        :return: The total of this InlineResponse2006.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse2006.


        :param total: The total of this InlineResponse2006.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def allow_next(self):
        """Gets the allow_next of this InlineResponse2006.  # noqa: E501


        :return: The allow_next of this InlineResponse2006.  # noqa: E501
        :rtype: bool
        """
        return self._allow_next

    @allow_next.setter
    def allow_next(self, allow_next):
        """Sets the allow_next of this InlineResponse2006.


        :param allow_next: The allow_next of this InlineResponse2006.  # noqa: E501
        :type: bool
        """

        self._allow_next = allow_next

    @property
    def items(self):
        """Gets the items of this InlineResponse2006.  # noqa: E501


        :return: The items of this InlineResponse2006.  # noqa: E501
        :rtype: list[InlineResponse2006Items]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InlineResponse2006.


        :param items: The items of this InlineResponse2006.  # noqa: E501
        :type: list[InlineResponse2006Items]
        """

        self._items = items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse2006, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2006):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2006):
            return True

        return self.to_dict() != other.to_dict()
