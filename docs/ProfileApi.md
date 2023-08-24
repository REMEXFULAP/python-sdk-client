# swagger_client.ProfileApi

All URIs are relative to *https://remesita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v1_balance_get**](ProfileApi.md#rest_v1_balance_get) | **GET** /rest/v1/balance | Obtiene datos de balance
[**rest_v1_user_lockup_code_code_post**](ProfileApi.md#rest_v1_user_lockup_code_code_post) | **POST** /rest/v1/user/lockup-code/{code} | Obtener datos de un cliente a partir de su codigo de cliente/referidos


# **rest_v1_balance_get**
> InlineResponse2009 rest_v1_balance_get()

Obtiene datos de balance

Devuelve el balance y otros detalles relacionados

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try:
    # Obtiene datos de balance
    api_response = api_instance.rest_v1_balance_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->rest_v1_balance_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v1_user_lockup_code_code_post**
> rest_v1_user_lockup_code_code_post(code)

Obtener datos de un cliente a partir de su codigo de cliente/referidos

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    # Obtener datos de un cliente a partir de su codigo de cliente/referidos
    api_instance.rest_v1_user_lockup_code_code_post(code)
except ApiException as e:
    print("Exception when calling ProfileApi->rest_v1_user_lockup_code_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

