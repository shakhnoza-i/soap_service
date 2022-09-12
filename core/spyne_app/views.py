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
    @rpc(Unicode(nillable=False), _returns=Unicode)
    def hello(ctx, name):
        return 'Hello, {}'.format(name)

    # There are 2 input parameters and both of them are not null integers, 
    # the output is also an integer.
    @rpc(Integer(nillable=False), Integer(nillable=False), _returns=Integer)
    def sum(ctx, a, b):
        return int(a + b)


# A SOAP application should be created to wrap SOAP services, the services should be 
# listed as the first argument of spyne.application.Application constructor, base on 
# our implementation the list is [SoapService].
soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
