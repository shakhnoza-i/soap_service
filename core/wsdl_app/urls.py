from django.urls import path

from wsdl_app.views import my_soap_application

urlpatterns = [
    path('', my_soap_application),
]
