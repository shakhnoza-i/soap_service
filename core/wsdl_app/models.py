from spyne.model.primitive import Unicode
from spyne.model.complex import ComplexModelBase, ComplexModel, ComplexModelMeta


class AsyncSendMessageRequest(ComplexModel): 
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
""" Сейчас: <xs:complexType name="AsyncSendMessageRequest"/>
<xs:element name="AsyncSendMessageRequest" type="s1:AsyncSendMessageRequest"/>
Нужно прописать элементы как в xsd схеме, чтобы сам комплексный тип по дефолту не ставился"""


class AsyncSendMessageResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    doc='Question'
    class Attributes(ComplexModel.Attributes):
        wsdl_part_name = 'Msg'


class AsyncSendDeliveryNotificationRequest(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'


class AsyncSendDeliveryNotificationResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'


# class AsyncSendMessage(ComplexModel):
#     __type_name__ = 'AsyncSendMessageRequest'
#     doc = 'Ответ'
#     AsyncSendMessageResponse = Unicode(doc="The name of an existing map to be included in this order")
#     class Attributes(ComplexModel.Attributes):
#         declare_order = 'declared' 
#         name = 'request'


class Common(ComplexModel):
    request = AsyncSendMessageRequest(doc='Question')
    response = AsyncSendMessageResponse(doc='Answer')
