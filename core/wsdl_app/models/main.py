from spyne.model.primitive import Unicode, DateTime
from spyne.model.complex import ComplexModel, Array

from .common import ErrorInfo, MessageData, guid
from .async_specific import AsyncMessageInfo


class AsyncSendMessageRequest(ComplexModel): 
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    messageInfo = AsyncMessageInfo
    messageData = MessageData
    class Attributes(ComplexModel.Attributes):
        min_occurs=1
        doc = 'Запрос'


class AsyncSendMessageResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    messageId = Unicode(doc='Идентификатор сообщения', min_occurs=1, nillable=False)
    correlationId = Unicode(doc='Идентификатор цепочки сообщения', min_occurs=1, nillable=False)
    responseDate = DateTime(doc='Дата ответа', min_occurs=1, nillable=False)
    sessionId = guid
    class Attributes(ComplexModel.Attributes):
        in_body_doc = 'Ответ'
        min_occurs=1
        declare_order = 'declared'


class AsyncSendDeliveryNotificationRequest(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    class Attributes(ComplexModel.Attributes):
        min_occurs=1
        

class AsyncSendDeliveryNotificationResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    class Attributes(ComplexModel.Attributes):
        min_occurs=1


class sendMessageFault1_sendMessageFault(ErrorInfo):
    _type_name__="sendMessageFault1_sendMessageFault"

class sendDeliveryNotificationFault1_sendDeliveryNotificationFault(ErrorInfo):
    __type_name__="sendDeliveryNotificationFault1_sendDeliveryNotificationFault"

