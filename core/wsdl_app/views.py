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


class SoapService(ServiceBase):


    @rpc(AsyncSendMessageRequest, 
    _returns=AsyncSendMessageResponse,
    _out_variable_name='response',
    # _in_message_name='sendMessageRequestMsg',
    # _out_message_name='sendMessageResponseMsg',
    _faults=ErrorInfo,
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
    [SoapService],
    name='IAsyncChannel',
    tns='http://bip.bee.kz/AsyncChannel/v10/Interfaces',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
