from spyne.model.primitive import Unicode
from spyne.model.complex import ComplexModelBase, ComplexModel, ComplexModelMeta


# class EmailString(Unicode):
#     __type_name__ = 'EmailString'

#     class Attributes(Unicode.Attributes):
#         max_length = 128
#         pattern = '[^@]+@[^@]+'


class AsyncSendMessageRequest(ComplexModel): 
    __namespace__ = 'http://bip.bee.kz/common/v10/Types' 
""" Сейчас: <xs:complexType name="AsyncSendMessageRequest"/>
<xs:element name="AsyncSendMessageRequest" type="s1:AsyncSendMessageRequest"/>
Нужно прописать элементы как в xsd схеме, чтобы сам комплексный тип по дефолту не ставился"""


class AsyncSendMessageResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    schema_location = 'AsyncSendMessageRequest.xsd'


class AsyncSendDeliveryNotificationRequest(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'


class AsyncSendDeliveryNotificationResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'


# class AsyncSendMessage(ComplexModel):
#     __type_name__ = 'AsyncSendMessageRequest'
#     class Attributes(ComplexModel.Attributes):
#         declare_order = 'declared' 
#         name = 'request'
