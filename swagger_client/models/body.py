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


class Body(object):
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
        '_from': 'str',
        'to': 'str',
        'amount': 'float',
        'currency': 'str',
        'memo': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'amount': 'amount',
        'currency': 'currency',
        'memo': 'memo'
    }

    def __init__(self, _from=None, to=None, amount=None, currency=None, memo=None, _configuration=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__from = None
        self._to = None
        self._amount = None
        self._currency = None
        self._memo = None
        self.discriminator = None

        self._from = _from
        self.to = to
        self.amount = amount
        if currency is not None:
            self.currency = currency
        self.memo = memo

    @property
    def _from(self):
        """Gets the _from of this Body.  # noqa: E501

        Número de tarjeta Visa de origen  # noqa: E501

        :return: The _from of this Body.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Body.

        Número de tarjeta Visa de origen  # noqa: E501

        :param _from: The _from of this Body.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this Body.  # noqa: E501

        Número de tarjeta Visa de destino  # noqa: E501

        :return: The to of this Body.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Body.

        Número de tarjeta Visa de destino  # noqa: E501

        :param to: The to of this Body.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def amount(self):
        """Gets the amount of this Body.  # noqa: E501

        Monto a transferir  # noqa: E501

        :return: The amount of this Body.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Body.

        Monto a transferir  # noqa: E501

        :param amount: The amount of this Body.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Body.  # noqa: E501

        Moneda de la transferencia (MXN o USD). Si no se envía, se asume USD por defecto.  # noqa: E501

        :return: The currency of this Body.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Body.

        Moneda de la transferencia (MXN o USD). Si no se envía, se asume USD por defecto.  # noqa: E501

        :param currency: The currency of this Body.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def memo(self):
        """Gets the memo of this Body.  # noqa: E501

        Comentario o concepto de la transacción  # noqa: E501

        :return: The memo of this Body.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this Body.

        Comentario o concepto de la transacción  # noqa: E501

        :param memo: The memo of this Body.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and memo is None:
            raise ValueError("Invalid value for `memo`, must not be `None`")  # noqa: E501

        self._memo = memo

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Body):
            return True

        return self.to_dict() != other.to_dict()