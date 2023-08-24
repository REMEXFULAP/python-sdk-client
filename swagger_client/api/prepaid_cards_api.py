# coding: utf-8

"""
    REMESITA API REST

    Api de remesita.com para desarrolladores. Primero obten tu apiKey y apiSecret, y para autenticarte debes ejecutar el endpoint rest/v1/auth en la respuesta obtendrás un token de acceso que debes usar en el resto de peticiones  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PrepaidCardsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rest_v1_card_number_toggle_post(self, number, **kwargs):  # noqa: E501
        """Bloquea o desbloquea una tarjeta  # noqa: E501

        Cambia el estado de bloqueo de una tarjeta específica  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_card_number_toggle_post(number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str number: Número de tarjeta (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v1_card_number_toggle_post_with_http_info(number, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v1_card_number_toggle_post_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def rest_v1_card_number_toggle_post_with_http_info(self, number, **kwargs):  # noqa: E501
        """Bloquea o desbloquea una tarjeta  # noqa: E501

        Cambia el estado de bloqueo de una tarjeta específica  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_card_number_toggle_post_with_http_info(number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str number: Número de tarjeta (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v1_card_number_toggle_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in params or
                                                       params['number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `number` when calling `rest_v1_card_number_toggle_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/card/{number}/toggle', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v1_card_number_transactions_pg_pg_size_get(self, number, pg, pg_size, **kwargs):  # noqa: E501
        """Obtiene las transacciones de una tarjeta  # noqa: E501

        Recupera una lista paginada de transacciones para una tarjeta específica  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_card_number_transactions_pg_pg_size_get(number, pg, pg_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str number: Número de tarjeta (required)
        :param int pg: Número de página (required)
        :param int pg_size: Tamaño de página (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v1_card_number_transactions_pg_pg_size_get_with_http_info(number, pg, pg_size, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v1_card_number_transactions_pg_pg_size_get_with_http_info(number, pg, pg_size, **kwargs)  # noqa: E501
            return data

    def rest_v1_card_number_transactions_pg_pg_size_get_with_http_info(self, number, pg, pg_size, **kwargs):  # noqa: E501
        """Obtiene las transacciones de una tarjeta  # noqa: E501

        Recupera una lista paginada de transacciones para una tarjeta específica  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_card_number_transactions_pg_pg_size_get_with_http_info(number, pg, pg_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str number: Número de tarjeta (required)
        :param int pg: Número de página (required)
        :param int pg_size: Tamaño de página (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number', 'pg', 'pg_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v1_card_number_transactions_pg_pg_size_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in params or
                                                       params['number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `number` when calling `rest_v1_card_number_transactions_pg_pg_size_get`")  # noqa: E501
        # verify the required parameter 'pg' is set
        if self.api_client.client_side_validation and ('pg' not in params or
                                                       params['pg'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `pg` when calling `rest_v1_card_number_transactions_pg_pg_size_get`")  # noqa: E501
        # verify the required parameter 'pg_size' is set
        if self.api_client.client_side_validation and ('pg_size' not in params or
                                                       params['pg_size'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `pg_size` when calling `rest_v1_card_number_transactions_pg_pg_size_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501
        if 'pg' in params:
            path_params['pg'] = params['pg']  # noqa: E501
        if 'pg_size' in params:
            path_params['pgSize'] = params['pg_size']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/card/{number}/transactions/{pg}/{pgSize}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v1_card_transfer_between_post(self, body, **kwargs):  # noqa: E501
        """Transfiere saldo entre cuentas Remesita  # noqa: E501

        Permite transferir saldo entre dos cuentas Remesita especificadas por los números de tarjeta Visa.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_card_transfer_between_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: Detalles de la transferencia (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v1_card_transfer_between_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.rest_v1_card_transfer_between_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def rest_v1_card_transfer_between_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Transfiere saldo entre cuentas Remesita  # noqa: E501

        Permite transferir saldo entre dos cuentas Remesita especificadas por los números de tarjeta Visa.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_card_transfer_between_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: Detalles de la transferencia (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v1_card_transfer_between_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `rest_v1_card_transfer_between_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/card/transfer-between', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rest_v1_cards_get(self, **kwargs):  # noqa: E501
        """Obtiene la lista de tarjetas prepagadas  # noqa: E501

        Devuelve una lista de todas las tarjetas prepagadas en el sistema  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_cards_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rest_v1_cards_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.rest_v1_cards_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def rest_v1_cards_get_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene la lista de tarjetas prepagadas  # noqa: E501

        Devuelve una lista de todas las tarjetas prepagadas en el sistema  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rest_v1_cards_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rest_v1_cards_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/rest/v1/cards', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)