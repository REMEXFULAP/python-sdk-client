# swagger_client.OperationsApi

All URIs are relative to *https://remesita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v1_operation_orders_get**](OperationsApi.md#rest_v1_operation_orders_get) | **GET** /rest/v1/operation/orders | Obtiene una lista de órdenes
[**rest_v1_operation_p2p_get**](OperationsApi.md#rest_v1_operation_p2p_get) | **GET** /rest/v1/operation/p2p | Obtiene una lista de operaciones P2P


# **rest_v1_operation_orders_get**
> InlineResponse2005 rest_v1_operation_orders_get(pg=pg, pg_size=pg_size, start=start, end=end, status=status)

Obtiene una lista de órdenes

Recupera una lista paginada de órdenes

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
pg = 1 # int | Número de página (optional) (default to 1)
pg_size = 25 # int | Cantidad de elementos por página (optional) (default to 25)
start = '2023-01-01' # datetime | Fecha de inicio en formato Y-m-d H:i:s (optional) (default to 2023-01-01)
end = '2025-01-01' # datetime | Fecha de finalización en formato Y-m-d H:i:s (optional) (default to 2025-01-01)
status = 'status_example' # str | Estado para filtrar (optional)

try:
    # Obtiene una lista de órdenes
    api_response = api_instance.rest_v1_operation_orders_get(pg=pg, pg_size=pg_size, start=start, end=end, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->rest_v1_operation_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pg** | **int**| Número de página | [optional] [default to 1]
 **pg_size** | **int**| Cantidad de elementos por página | [optional] [default to 25]
 **start** | **datetime**| Fecha de inicio en formato Y-m-d H:i:s | [optional] [default to 2023-01-01]
 **end** | **datetime**| Fecha de finalización en formato Y-m-d H:i:s | [optional] [default to 2025-01-01]
 **status** | **str**| Estado para filtrar | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v1_operation_p2p_get**
> InlineResponse2006 rest_v1_operation_p2p_get(pg=pg, pg_size=pg_size, start=start, end=end)

Obtiene una lista de operaciones P2P

Recupera una lista paginada de operaciones P2P

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
pg = 1 # int | Número de página (optional) (default to 1)
pg_size = 25 # int | Cantidad de elementos por página (optional) (default to 25)
start = '2022-01-01' # datetime | Fecha de inicio en formato Y-m-d H:i:s (optional) (default to 2022-01-01)
end = '2025-01-01' # datetime | Fecha de finalización en formato Y-m-d H:i:s (optional) (default to 2025-01-01)

try:
    # Obtiene una lista de operaciones P2P
    api_response = api_instance.rest_v1_operation_p2p_get(pg=pg, pg_size=pg_size, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->rest_v1_operation_p2p_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pg** | **int**| Número de página | [optional] [default to 1]
 **pg_size** | **int**| Cantidad de elementos por página | [optional] [default to 25]
 **start** | **datetime**| Fecha de inicio en formato Y-m-d H:i:s | [optional] [default to 2022-01-01]
 **end** | **datetime**| Fecha de finalización en formato Y-m-d H:i:s | [optional] [default to 2025-01-01]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

