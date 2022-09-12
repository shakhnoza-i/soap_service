from django.urls import path

from spyne_app.views import my_soap_application

urlpatterns = [
    path('soap_service/', my_soap_application),
]
