from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

from .models import (AsyncSendMessageRequest, AsyncSendMessageResponse, 
AsyncSendDeliveryNotificationRequest, AsyncSendDeliveryNotificationResponse,
sendMessageFault1_sendMessageFault, sendDeliveryNotificationFault1_sendDeliveryNotificationFault)


class AsyncChannelHttpService(ServiceBase):


    @rpc(AsyncSendMessageRequest, 
    _returns=AsyncSendMessageResponse,
    _out_variable_name='response',
    _faults=sendMessageFault1_sendMessageFault,
    )
    def sendMessage(ctx, request):
        response = 'Hello, {}'.format(request)
        return response


    @rpc(AsyncSendDeliveryNotificationRequest, 
    _returns=AsyncSendDeliveryNotificationResponse, 
    _out_variable_name='response',
    _faults=sendDeliveryNotificationFault1_sendDeliveryNotificationFault,
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
