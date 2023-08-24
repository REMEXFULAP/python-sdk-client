# swagger_client.AuthenticationApi

All URIs are relative to *https://remesita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v1_auth_post**](AuthenticationApi.md#rest_v1_auth_post) | **POST** /rest/v1/auth | Autentica al usuario con api_key y api_secret


# **rest_v1_auth_post**
> InlineResponse2008 rest_v1_auth_post(body)

Autentica al usuario con api_key y api_secret

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
api_instance = swagger_client.AuthenticationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body2() # Body2 | JSON con api_key y api_secret

try:
    # Autentica al usuario con api_key y api_secret
    api_response = api_instance.rest_v1_auth_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->rest_v1_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| JSON con api_key y api_secret | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

