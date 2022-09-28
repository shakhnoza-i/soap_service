# coding=utf-8

from suds.client import Client
from suds.cache import NoCache


my_client = Client('http://127.0.0.1:8000/spyne/soap_service/?WSDL', cache=NoCache())
# print (my_client)
# print ('Function hello: ', my_client.service.hello('Minh'))
# print ('Function sum: ', my_client.service.sum(10, 20))

"""
Service ( SoapService ) tns="django.soap.example"
   Prefixes (1)
      ns0 = "django.soap.example"
   Ports (1):
      (Application)
         Methods (2):
            hello(xs:string name)
            sum(xs:integer a, xs:integer b)
         Types (4):
            hello
            helloResponse
            sum
            sumResponse

Function hello:  Hello, Minh
Function sum:  30
"""


custom_client = Client('http://127.0.0.1:8000/app/?WSDL', cache=NoCache())
print(custom_client)

"""
Service ( AsyncChannelHttpService ) tns="http://bip.bee.kz/AsyncChannel/v10/Interfaces"
   Prefixes (2)
      ns0 = "http://bip.bee.kz/AsyncChannel/v10/ITypes"
      ns1 = "http://bip.bee.kz/AsyncChannel/v10/Interfaces"
   Ports (1):
      (IAsyncChannel)
         Methods (1):
            sendMessage(ns0:AsyncSendMessageRequest request)
         Types (4):
            ns0:AsyncSendMessageRequest
            ns0:AsyncSendMessageResponse
            sendMessage
            sendMessageResponse
"""