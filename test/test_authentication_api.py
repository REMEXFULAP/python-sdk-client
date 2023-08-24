# coding: utf-8

"""
    REMESITA API REST

    Api de remesita.com para desarrolladores. Primero obten tu apiKey y apiSecret, y para autenticarte debes ejecutar el endpoint rest/v1/auth en la respuesta obtendrás un token de acceso que debes usar en el resto de peticiones  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.authentication_api import AuthenticationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rest_v1_auth_post(self):
        """Test case for rest_v1_auth_post

        Autentica al usuario con api_key y api_secret  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()