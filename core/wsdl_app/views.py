from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

from wsdl_app.models import (AsyncSendMessageRequest, AsyncSendMessageResponse, 
AsyncSendDeliveryNotificationRequest, AsyncSendDeliveryNotificationResponse)


class SoapService(ServiceBase):
    # rpc is method decorator to tag a method as a remote procedure call 
    # in a spyne.service.ServiceBase subclass.

    # There is one input parameter and parse it as a Unicode string, cannot be null; 
    # there output is a Unicode string, too.
    @rpc(AsyncSendMessageRequest, _returns=AsyncSendMessageResponse)
    def sendMessage(ctx, request):
        response = 'Hello, {}'.format(request)
        return response

    @rpc(AsyncSendDeliveryNotificationRequest, _returns=AsyncSendDeliveryNotificationResponse)
    def sendDeliveryNotification(ctx, request):
        print(request)


soap_app = Application(
    [SoapService],
    name='IAsyncChannel_N',
    tns='http://bip.bee.kz/AsyncChannel/v10/Interfaces',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
