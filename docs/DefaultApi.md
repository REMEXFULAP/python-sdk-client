# swagger_client.DefaultApi

All URIs are relative to *https://remesita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v1_user_lockup_code_code_get**](DefaultApi.md#rest_v1_user_lockup_code_code_get) | **GET** /rest/v1/user/lockup-code/{code} | Obtener datos de un cliente a partir de su codigo de cliente/referidos


# **rest_v1_user_lockup_code_code_get**
> rest_v1_user_lockup_code_code_get(code)

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | 

try:
    # Obtener datos de un cliente a partir de su codigo de cliente/referidos
    api_instance.rest_v1_user_lockup_code_code_get(code)
except ApiException as e:
    print("Exception when calling DefaultApi->rest_v1_user_lockup_code_code_get: %s\n" % e)
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

