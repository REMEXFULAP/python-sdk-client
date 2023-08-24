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


class InlineResponse2003Items(object):
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
        'id': 'int',
        'type': 'str',
        '_date': 'str',
        'amount': 'float',
        'amount_usd': 'float',
        'exchange_rate': 'float',
        'currency': 'str',
        'memo': 'str',
        'category': 'str',
        'payee': 'str',
        'website': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        '_date': 'date',
        'amount': 'amount',
        'amount_usd': 'amountUSD',
        'exchange_rate': 'exchangeRate',
        'currency': 'currency',
        'memo': 'memo',
        'category': 'category',
        'payee': 'payee',
        'website': 'website',
        'status': 'status'
    }

    def __init__(self, id=None, type=None, _date=None, amount=None, amount_usd=None, exchange_rate=None, currency=None, memo=None, category=None, payee=None, website=None, status=None, _configuration=None):  # noqa: E501
        """InlineResponse2003Items - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self.__date = None
        self._amount = None
        self._amount_usd = None
        self._exchange_rate = None
        self._currency = None
        self._memo = None
        self._category = None
        self._payee = None
        self._website = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if _date is not None:
            self._date = _date
        if amount is not None:
            self.amount = amount
        if amount_usd is not None:
            self.amount_usd = amount_usd
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if currency is not None:
            self.currency = currency
        if memo is not None:
            self.memo = memo
        if category is not None:
            self.category = category
        if payee is not None:
            self.payee = payee
        if website is not None:
            self.website = website
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this InlineResponse2003Items.  # noqa: E501


        :return: The id of this InlineResponse2003Items.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2003Items.


        :param id: The id of this InlineResponse2003Items.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this InlineResponse2003Items.  # noqa: E501


        :return: The type of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2003Items.


        :param type: The type of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def _date(self):
        """Gets the _date of this InlineResponse2003Items.  # noqa: E501


        :return: The _date of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InlineResponse2003Items.


        :param _date: The _date of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def amount(self):
        """Gets the amount of this InlineResponse2003Items.  # noqa: E501


        :return: The amount of this InlineResponse2003Items.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse2003Items.


        :param amount: The amount of this InlineResponse2003Items.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def amount_usd(self):
        """Gets the amount_usd of this InlineResponse2003Items.  # noqa: E501


        :return: The amount_usd of this InlineResponse2003Items.  # noqa: E501
        :rtype: float
        """
        return self._amount_usd

    @amount_usd.setter
    def amount_usd(self, amount_usd):
        """Sets the amount_usd of this InlineResponse2003Items.


        :param amount_usd: The amount_usd of this InlineResponse2003Items.  # noqa: E501
        :type: float
        """

        self._amount_usd = amount_usd

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this InlineResponse2003Items.  # noqa: E501


        :return: The exchange_rate of this InlineResponse2003Items.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this InlineResponse2003Items.


        :param exchange_rate: The exchange_rate of this InlineResponse2003Items.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def currency(self):
        """Gets the currency of this InlineResponse2003Items.  # noqa: E501


        :return: The currency of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse2003Items.


        :param currency: The currency of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def memo(self):
        """Gets the memo of this InlineResponse2003Items.  # noqa: E501


        :return: The memo of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this InlineResponse2003Items.


        :param memo: The memo of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def category(self):
        """Gets the category of this InlineResponse2003Items.  # noqa: E501


        :return: The category of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this InlineResponse2003Items.


        :param category: The category of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def payee(self):
        """Gets the payee of this InlineResponse2003Items.  # noqa: E501


        :return: The payee of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self._payee

    @payee.setter
    def payee(self, payee):
        """Sets the payee of this InlineResponse2003Items.


        :param payee: The payee of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self._payee = payee

    @property
    def website(self):
        """Gets the website of this InlineResponse2003Items.  # noqa: E501


        :return: The website of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this InlineResponse2003Items.


        :param website: The website of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def status(self):
        """Gets the status of this InlineResponse2003Items.  # noqa: E501


        :return: The status of this InlineResponse2003Items.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2003Items.


        :param status: The status of this InlineResponse2003Items.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(InlineResponse2003Items, dict):
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
        if not isinstance(other, InlineResponse2003Items):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2003Items):
            return True

        return self.to_dict() != other.to_dict()