from django.urls import path

from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView

from example_app.views import hello_world_service, app, HelloWorldService


urlpatterns = [
    path(r'^hello_world/', hello_world_service),
    # path(r'^say_hello/', DjangoView.as_view(
    #     services=[HelloWorldService], tns='spyne.examples.django',
    #     in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
    # path(r'^say_hello_not_cached/', DjangoView.as_view(
    #     services=[HelloWorldService], tns='spyne.examples.django',
    #     in_protocol=Soap11(validator='lxml'), out_protocol=Soap11(),
    #     cache_wsdl=False)),
    # path(r'^api/', DjangoView.as_view(application=app)),
]