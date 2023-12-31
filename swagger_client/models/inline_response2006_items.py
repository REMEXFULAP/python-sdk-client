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


class InlineResponse2006Items(object):
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
        'match': 'bool',
        'status': 'str',
        'order': 'str',
        'created_at': 'datetime',
        'completed_at': 'datetime',
        'payment_method': 'str',
        'sku': 'str',
        'quotation': 'float',
        'quotation_currency': 'str',
        'recipient_account': 'str',
        'recipient_amount': 'float'
    }

    attribute_map = {
        'match': 'match',
        'status': 'status',
        'order': 'order',
        'created_at': 'createdAt',
        'completed_at': 'completedAt',
        'payment_method': 'paymentMethod',
        'sku': 'sku',
        'quotation': 'quotation',
        'quotation_currency': 'quotationCurrency',
        'recipient_account': 'recipientAccount',
        'recipient_amount': 'recipientAmount'
    }

    def __init__(self, match=None, status=None, order=None, created_at=None, completed_at=None, payment_method=None, sku=None, quotation=None, quotation_currency=None, recipient_account=None, recipient_amount=None, _configuration=None):  # noqa: E501
        """InlineResponse2006Items - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._match = None
        self._status = None
        self._order = None
        self._created_at = None
        self._completed_at = None
        self._payment_method = None
        self._sku = None
        self._quotation = None
        self._quotation_currency = None
        self._recipient_account = None
        self._recipient_amount = None
        self.discriminator = None

        if match is not None:
            self.match = match
        if status is not None:
            self.status = status
        if order is not None:
            self.order = order
        if created_at is not None:
            self.created_at = created_at
        if completed_at is not None:
            self.completed_at = completed_at
        if payment_method is not None:
            self.payment_method = payment_method
        if sku is not None:
            self.sku = sku
        if quotation is not None:
            self.quotation = quotation
        if quotation_currency is not None:
            self.quotation_currency = quotation_currency
        if recipient_account is not None:
            self.recipient_account = recipient_account
        if recipient_amount is not None:
            self.recipient_amount = recipient_amount

    @property
    def match(self):
        """Gets the match of this InlineResponse2006Items.  # noqa: E501


        :return: The match of this InlineResponse2006Items.  # noqa: E501
        :rtype: bool
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this InlineResponse2006Items.


        :param match: The match of this InlineResponse2006Items.  # noqa: E501
        :type: bool
        """

        self._match = match

    @property
    def status(self):
        """Gets the status of this InlineResponse2006Items.  # noqa: E501


        :return: The status of this InlineResponse2006Items.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2006Items.


        :param status: The status of this InlineResponse2006Items.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def order(self):
        """Gets the order of this InlineResponse2006Items.  # noqa: E501


        :return: The order of this InlineResponse2006Items.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this InlineResponse2006Items.


        :param order: The order of this InlineResponse2006Items.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2006Items.  # noqa: E501


        :return: The created_at of this InlineResponse2006Items.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2006Items.


        :param created_at: The created_at of this InlineResponse2006Items.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def completed_at(self):
        """Gets the completed_at of this InlineResponse2006Items.  # noqa: E501


        :return: The completed_at of this InlineResponse2006Items.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this InlineResponse2006Items.


        :param completed_at: The completed_at of this InlineResponse2006Items.  # noqa: E501
        :type: datetime
        """

        self._completed_at = completed_at

    @property
    def payment_method(self):
        """Gets the payment_method of this InlineResponse2006Items.  # noqa: E501


        :return: The payment_method of this InlineResponse2006Items.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this InlineResponse2006Items.


        :param payment_method: The payment_method of this InlineResponse2006Items.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def sku(self):
        """Gets the sku of this InlineResponse2006Items.  # noqa: E501


        :return: The sku of this InlineResponse2006Items.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this InlineResponse2006Items.


        :param sku: The sku of this InlineResponse2006Items.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def quotation(self):
        """Gets the quotation of this InlineResponse2006Items.  # noqa: E501


        :return: The quotation of this InlineResponse2006Items.  # noqa: E501
        :rtype: float
        """
        return self._quotation

    @quotation.setter
    def quotation(self, quotation):
        """Sets the quotation of this InlineResponse2006Items.


        :param quotation: The quotation of this InlineResponse2006Items.  # noqa: E501
        :type: float
        """

        self._quotation = quotation

    @property
    def quotation_currency(self):
        """Gets the quotation_currency of this InlineResponse2006Items.  # noqa: E501


        :return: The quotation_currency of this InlineResponse2006Items.  # noqa: E501
        :rtype: str
        """
        return self._quotation_currency

    @quotation_currency.setter
    def quotation_currency(self, quotation_currency):
        """Sets the quotation_currency of this InlineResponse2006Items.


        :param quotation_currency: The quotation_currency of this InlineResponse2006Items.  # noqa: E501
        :type: str
        """

        self._quotation_currency = quotation_currency

    @property
    def recipient_account(self):
        """Gets the recipient_account of this InlineResponse2006Items.  # noqa: E501


        :return: The recipient_account of this InlineResponse2006Items.  # noqa: E501
        :rtype: str
        """
        return self._recipient_account

    @recipient_account.setter
    def recipient_account(self, recipient_account):
        """Sets the recipient_account of this InlineResponse2006Items.


        :param recipient_account: The recipient_account of this InlineResponse2006Items.  # noqa: E501
        :type: str
        """

        self._recipient_account = recipient_account

    @property
    def recipient_amount(self):
        """Gets the recipient_amount of this InlineResponse2006Items.  # noqa: E501


        :return: The recipient_amount of this InlineResponse2006Items.  # noqa: E501
        :rtype: float
        """
        return self._recipient_amount

    @recipient_amount.setter
    def recipient_amount(self, recipient_amount):
        """Sets the recipient_amount of this InlineResponse2006Items.


        :param recipient_amount: The recipient_amount of this InlineResponse2006Items.  # noqa: E501
        :type: float
        """

        self._recipient_amount = recipient_amount

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
        if issubclass(InlineResponse2006Items, dict):
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
        if not isinstance(other, InlineResponse2006Items):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2006Items):
            return True

        return self.to_dict() != other.to_dict()
