from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase


class SoapService(ServiceBase):
    # rpc is method decorator to tag a method as a remote procedure call 
    # in a spyne.service.ServiceBase subclass.

    # There is one input parameter and parse it as a Unicode string, cannot be null; 
    # there output is a Unicode string, too.
    @rpc(Unicode(request="request", nillable=True, __type_name__="bons3:AsyncSendMessageRequest"), _returns=Unicode)
    def sendMessage(ctx, name):
        return 'Hello, {}'.format(name)

    @rpc(Integer(nillable=False), Integer(nillable=False), _returns=Integer)
    def sum(ctx, a, b):
        return int(a + b)

    @rpc(Integer(nillable=False), Integer(nillable=False), _returns=Integer)
    def subtr(ctx, a, b):
        return int(a - b)


# A SOAP application should be created to wrap SOAP services, the services should be 
# listed as the first argument of spyne.application.Application constructor, base on 
# our implementation the list is [SoapService].
soap_app = Application(
    [SoapService],
    name='IAsyncChannel_N',
    tns='http://bip.bee.kz/AsyncChannel/v10/Interfaces',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
