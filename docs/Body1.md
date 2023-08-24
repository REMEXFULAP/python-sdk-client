# Body1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_unit_id** | **str** | ID del negocio que está generando el link de pago | 
**amount** | **float** | Monto a pagar | 
**concept** | **str** | Concepto de pago o comentario | 
**ipn_url** | **str** | Dirección para recibir webhooks de notificaciones de pago en segundo plano | [optional] 
**success_url** | **str** | URL a donde redireccionar si el pago es satisfactorio | [optional] 
**cancel_url** | **str** | URL a donde redireccionar si el pago es cancelado | [optional] 
**custom_id** | **str** | Identificador externo para trazabilidad | [optional] 
**payer_name** | **str** | Nombre del pagador (si se conoce) | [optional] 
**payer_phone** | **str** | Teléfono del pagador (si se conoce) | [optional] 
**payer_email** | **str** | Email del pagador (si se conoce) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


