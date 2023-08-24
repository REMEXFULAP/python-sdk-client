# swagger_client.BusinessApi

All URIs are relative to *https://remesita.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v1_business_get**](BusinessApi.md#rest_v1_business_get) | **GET** /rest/v1/business | Obtiene la lista de negocios registrados
[**rest_v1_payment_link_post**](BusinessApi.md#rest_v1_payment_link_post) | **POST** /rest/v1/payment-link | Genera un link de pago


# **rest_v1_business_get**
> list[InlineResponse200] rest_v1_business_get()

Obtiene la lista de negocios registrados

Devuelve una lista de todos los negocios registrados en remesita

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
api_instance = swagger_client.BusinessApi(swagger_client.ApiClient(configuration))

try:
    # Obtiene la lista de negocios registrados
    api_response = api_instance.rest_v1_business_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessApi->rest_v1_business_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v1_payment_link_post**
> InlineResponse2007 rest_v1_payment_link_post(body)

Genera un link de pago

Crea un link de pago basado en los detalles proporcionados

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
api_instance = swagger_client.BusinessApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body1() # Body1 | Detalles para generar el link de pago

try:
    # Genera un link de pago
    api_response = api_instance.rest_v1_payment_link_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessApi->rest_v1_payment_link_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| Detalles para generar el link de pago | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

