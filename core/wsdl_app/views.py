from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.fault import Fault
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

from wsdl_app.models import (AsyncSendMessageRequest, AsyncSendMessageResponse, 
AsyncSendDeliveryNotificationRequest, AsyncSendDeliveryNotificationResponse,
ErrorInfo)


class AsyncChannelHttpService(ServiceBase):


    @rpc(AsyncSendMessageRequest, 
    _returns=AsyncSendMessageResponse,
    _out_variable_name='response',
    _throws=ErrorInfo, # _faults works as _throws
# _in_message_name='sendMessageRequestMsg', - change class name everywhere
# _out_message_name='sendMessageResponseMsg',
# _args=['bazon','bazon2','bazon3','bazon4','bazon5',]  -  spyne.LogicError: 'sendMessage' function has 5 argument(s) but the _args argument has 1
# _event_manager=ErrorInfo - nothing changed
# _event_managers=ErrorInfo - type object 'ErrorInfo' has no attribute 'append'
# _wsdl_part_name='sendMessageRequestMsg'  - changed <wsdl:part name both for request and response, but the are different
# _internal_key_suffix='question' - nothing changed
# _operation_name='question' - changed everywhere request method name (only method name, not class)
    )
    def sendMessage(ctx, request):
        response = 'Hello, {}'.format(request)
        return response


    @rpc(AsyncSendDeliveryNotificationRequest, 
    _returns=AsyncSendDeliveryNotificationResponse, 
    _out_variable_name='response',
    )
    def sendDeliveryNotification(ctx, request):
        print(request)


soap_app = Application(
    [AsyncChannelHttpService],
    name='IAsyncChannel',
    tns='http://bip.bee.kz/AsyncChannel/v10/Interfaces',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(cleanup_namespaces=True),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
