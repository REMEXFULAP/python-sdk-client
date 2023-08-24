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


class InlineResponse2004Items(object):
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
        'balance': 'float',
        'balance_formatted': 'str',
        'balance_usd': 'float',
        'balance_usd_formatted': 'str',
        'status': 'str',
        'number': 'str',
        'number_formatted': 'str',
        'exchange_rate': 'float',
        'clabe': 'str',
        'cash_reference': 'str',
        'locked': 'bool',
        'alias': 'str',
        'main': 'bool'
    }

    attribute_map = {
        'balance': 'balance',
        'balance_formatted': 'balanceFormatted',
        'balance_usd': 'balanceUSD',
        'balance_usd_formatted': 'balanceUSDFormatted',
        'status': 'status',
        'number': 'number',
        'number_formatted': 'numberFormatted',
        'exchange_rate': 'exchangeRate',
        'clabe': 'clabe',
        'cash_reference': 'cashReference',
        'locked': 'locked',
        'alias': 'alias',
        'main': 'main'
    }

    def __init__(self, balance=None, balance_formatted=None, balance_usd=None, balance_usd_formatted=None, status=None, number=None, number_formatted=None, exchange_rate=None, clabe=None, cash_reference=None, locked=None, alias=None, main=None, _configuration=None):  # noqa: E501
        """InlineResponse2004Items - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._balance = None
        self._balance_formatted = None
        self._balance_usd = None
        self._balance_usd_formatted = None
        self._status = None
        self._number = None
        self._number_formatted = None
        self._exchange_rate = None
        self._clabe = None
        self._cash_reference = None
        self._locked = None
        self._alias = None
        self._main = None
        self.discriminator = None

        if balance is not None:
            self.balance = balance
        if balance_formatted is not None:
            self.balance_formatted = balance_formatted
        if balance_usd is not None:
            self.balance_usd = balance_usd
        if balance_usd_formatted is not None:
            self.balance_usd_formatted = balance_usd_formatted
        if status is not None:
            self.status = status
        if number is not None:
            self.number = number
        if number_formatted is not None:
            self.number_formatted = number_formatted
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if clabe is not None:
            self.clabe = clabe
        if cash_reference is not None:
            self.cash_reference = cash_reference
        if locked is not None:
            self.locked = locked
        if alias is not None:
            self.alias = alias
        if main is not None:
            self.main = main

    @property
    def balance(self):
        """Gets the balance of this InlineResponse2004Items.  # noqa: E501

        Balance de la tarjeta  # noqa: E501

        :return: The balance of this InlineResponse2004Items.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this InlineResponse2004Items.

        Balance de la tarjeta  # noqa: E501

        :param balance: The balance of this InlineResponse2004Items.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def balance_formatted(self):
        """Gets the balance_formatted of this InlineResponse2004Items.  # noqa: E501

        Balance de la tarjeta formateado  # noqa: E501

        :return: The balance_formatted of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._balance_formatted

    @balance_formatted.setter
    def balance_formatted(self, balance_formatted):
        """Sets the balance_formatted of this InlineResponse2004Items.

        Balance de la tarjeta formateado  # noqa: E501

        :param balance_formatted: The balance_formatted of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._balance_formatted = balance_formatted

    @property
    def balance_usd(self):
        """Gets the balance_usd of this InlineResponse2004Items.  # noqa: E501

        Balance en USD  # noqa: E501

        :return: The balance_usd of this InlineResponse2004Items.  # noqa: E501
        :rtype: float
        """
        return self._balance_usd

    @balance_usd.setter
    def balance_usd(self, balance_usd):
        """Sets the balance_usd of this InlineResponse2004Items.

        Balance en USD  # noqa: E501

        :param balance_usd: The balance_usd of this InlineResponse2004Items.  # noqa: E501
        :type: float
        """

        self._balance_usd = balance_usd

    @property
    def balance_usd_formatted(self):
        """Gets the balance_usd_formatted of this InlineResponse2004Items.  # noqa: E501

        Balance en USD formateado  # noqa: E501

        :return: The balance_usd_formatted of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._balance_usd_formatted

    @balance_usd_formatted.setter
    def balance_usd_formatted(self, balance_usd_formatted):
        """Sets the balance_usd_formatted of this InlineResponse2004Items.

        Balance en USD formateado  # noqa: E501

        :param balance_usd_formatted: The balance_usd_formatted of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._balance_usd_formatted = balance_usd_formatted

    @property
    def status(self):
        """Gets the status of this InlineResponse2004Items.  # noqa: E501

        Estado de la tarjeta  # noqa: E501

        :return: The status of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2004Items.

        Estado de la tarjeta  # noqa: E501

        :param status: The status of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def number(self):
        """Gets the number of this InlineResponse2004Items.  # noqa: E501

        Número de la tarjeta  # noqa: E501

        :return: The number of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponse2004Items.

        Número de la tarjeta  # noqa: E501

        :param number: The number of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def number_formatted(self):
        """Gets the number_formatted of this InlineResponse2004Items.  # noqa: E501

        Número de la tarjeta formateado  # noqa: E501

        :return: The number_formatted of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._number_formatted

    @number_formatted.setter
    def number_formatted(self, number_formatted):
        """Sets the number_formatted of this InlineResponse2004Items.

        Número de la tarjeta formateado  # noqa: E501

        :param number_formatted: The number_formatted of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._number_formatted = number_formatted

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this InlineResponse2004Items.  # noqa: E501

        Tasa de cambio  # noqa: E501

        :return: The exchange_rate of this InlineResponse2004Items.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this InlineResponse2004Items.

        Tasa de cambio  # noqa: E501

        :param exchange_rate: The exchange_rate of this InlineResponse2004Items.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def clabe(self):
        """Gets the clabe of this InlineResponse2004Items.  # noqa: E501

        CLABE de la tarjeta  # noqa: E501

        :return: The clabe of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._clabe

    @clabe.setter
    def clabe(self, clabe):
        """Sets the clabe of this InlineResponse2004Items.

        CLABE de la tarjeta  # noqa: E501

        :param clabe: The clabe of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._clabe = clabe

    @property
    def cash_reference(self):
        """Gets the cash_reference of this InlineResponse2004Items.  # noqa: E501

        Referencia de efectivo  # noqa: E501

        :return: The cash_reference of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._cash_reference

    @cash_reference.setter
    def cash_reference(self, cash_reference):
        """Sets the cash_reference of this InlineResponse2004Items.

        Referencia de efectivo  # noqa: E501

        :param cash_reference: The cash_reference of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._cash_reference = cash_reference

    @property
    def locked(self):
        """Gets the locked of this InlineResponse2004Items.  # noqa: E501

        Indica si la tarjeta está bloqueada  # noqa: E501

        :return: The locked of this InlineResponse2004Items.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse2004Items.

        Indica si la tarjeta está bloqueada  # noqa: E501

        :param locked: The locked of this InlineResponse2004Items.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def alias(self):
        """Gets the alias of this InlineResponse2004Items.  # noqa: E501

        Alias de la tarjeta  # noqa: E501

        :return: The alias of this InlineResponse2004Items.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this InlineResponse2004Items.

        Alias de la tarjeta  # noqa: E501

        :param alias: The alias of this InlineResponse2004Items.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def main(self):
        """Gets the main of this InlineResponse2004Items.  # noqa: E501

        Indica si es la tarjeta principal  # noqa: E501

        :return: The main of this InlineResponse2004Items.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this InlineResponse2004Items.

        Indica si es la tarjeta principal  # noqa: E501

        :param main: The main of this InlineResponse2004Items.  # noqa: E501
        :type: bool
        """

        self._main = main

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
        if issubclass(InlineResponse2004Items, dict):
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
        if not isinstance(other, InlineResponse2004Items):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2004Items):
            return True

        return self.to_dict() != other.to_dict()
