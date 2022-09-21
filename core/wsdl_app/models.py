from email import message
from spyne.model.primitive import Unicode
from spyne.model.complex import ComplexModelBase, ComplexModel, ComplexModelMeta


class AsyncSendMessageRequest(ComplexModel): 
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    class Attributes(ComplexModel.Attributes):
        min_occurs=1


class AsyncSendMessageResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    messageId = Unicode(doc='Идентификатор сообщения', min_occurs=1, nillable=False)
    correlationId = Unicode(doc='Идентификатор цепочки сообщения', min_occurs=1, nillable=False)
    class Attributes(ComplexModel.Attributes):
        min_occurs=1


class AsyncSendDeliveryNotificationRequest(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    class Attributes(ComplexModel.Attributes):
        min_occurs=1


class AsyncSendDeliveryNotificationResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    class Attributes(ComplexModel.Attributes):
        min_occurs=1


# class AsyncSendMessage(ComplexModel):
#     __type_name__ = 'AsyncSendMessageRequest'
#     class Attributes(ComplexModel.Attributes):
#         declare_order = 'declared' 
#         name = 'request'
