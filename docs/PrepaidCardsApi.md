# swagger_client.PrepaidCardsApi

All URIs are relative to *https://remesita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v1_card_number_toggle_post**](PrepaidCardsApi.md#rest_v1_card_number_toggle_post) | **POST** /rest/v1/card/{number}/toggle | Bloquea o desbloquea una tarjeta
[**rest_v1_card_number_transactions_pg_pg_size_get**](PrepaidCardsApi.md#rest_v1_card_number_transactions_pg_pg_size_get) | **GET** /rest/v1/card/{number}/transactions/{pg}/{pgSize} | Obtiene las transacciones de una tarjeta
[**rest_v1_card_transfer_between_post**](PrepaidCardsApi.md#rest_v1_card_transfer_between_post) | **POST** /rest/v1/card/transfer-between | Transfiere saldo entre cuentas Remesita
[**rest_v1_cards_get**](PrepaidCardsApi.md#rest_v1_cards_get) | **GET** /rest/v1/cards | Obtiene la lista de tarjetas prepagadas


# **rest_v1_card_number_toggle_post**
> InlineResponse2002 rest_v1_card_number_toggle_post(number)

Bloquea o desbloquea una tarjeta

Cambia el estado de bloqueo de una tarjeta específica

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PrepaidCardsApi(swagger_client.ApiClient(configuration))
number = 'number_example' # str | Número de tarjeta

try:
    # Bloquea o desbloquea una tarjeta
    api_response = api_instance.rest_v1_card_number_toggle_post(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaidCardsApi->rest_v1_card_number_toggle_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Número de tarjeta | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v1_card_number_transactions_pg_pg_size_get**
> InlineResponse2003 rest_v1_card_number_transactions_pg_pg_size_get(number, pg, pg_size)

Obtiene las transacciones de una tarjeta

Recupera una lista paginada de transacciones para una tarjeta específica

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PrepaidCardsApi(swagger_client.ApiClient(configuration))
number = 'number_example' # str | Número de tarjeta
pg = 56 # int | Número de página
pg_size = 56 # int | Tamaño de página

try:
    # Obtiene las transacciones de una tarjeta
    api_response = api_instance.rest_v1_card_number_transactions_pg_pg_size_get(number, pg, pg_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaidCardsApi->rest_v1_card_number_transactions_pg_pg_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Número de tarjeta | 
 **pg** | **int**| Número de página | 
 **pg_size** | **int**| Tamaño de página | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v1_card_transfer_between_post**
> InlineResponse2001 rest_v1_card_transfer_between_post(body)

Transfiere saldo entre cuentas Remesita

Permite transferir saldo entre dos cuentas Remesita especificadas por los números de tarjeta Visa.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PrepaidCardsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body | Detalles de la transferencia

try:
    # Transfiere saldo entre cuentas Remesita
    api_response = api_instance.rest_v1_card_transfer_between_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaidCardsApi->rest_v1_card_transfer_between_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Detalles de la transferencia | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v1_cards_get**
> InlineResponse2004 rest_v1_cards_get()

Obtiene la lista de tarjetas prepagadas

Devuelve una lista de todas las tarjetas prepagadas en el sistema

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PrepaidCardsApi(swagger_client.ApiClient(configuration))

try:
    # Obtiene la lista de tarjetas prepagadas
    api_response = api_instance.rest_v1_cards_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrepaidCardsApi->rest_v1_cards_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

