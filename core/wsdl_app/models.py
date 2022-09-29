from email import message
from spyne.model.primitive import Unicode
from spyne.model.complex import ComplexModelBase, ComplexModel, ComplexModelMeta
from spyne.model.fault import Fault


class AsyncSendMessageRequest(ComplexModel): 
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    inletId = Unicode(doc='Входной идентификатор', min_occurs=1, nillable=False)
    class Attributes(ComplexModel.Attributes):
        min_occurs=1


class AsyncSendMessageResponse(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    in_body_doc = 'Ответ'
    messageId = Unicode(doc='Идентификатор сообщения', min_occurs=1, nillable=False)
    correlationId = Unicode(doc='Идентификатор цепочки сообщения', min_occurs=1, nillable=False)
    class Attributes(ComplexModel.Attributes):
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


class ErrorInfo(Fault):
    # __type_name__="sendMessageFault1_sendMessageFault"
    __namespace__ = 'http://bip.bee.kz/common/v10/Types' # не прописывается в WSDL схеме
    experimentFault = Unicode(doc='Сообщение об ошибке', min_occurs=1, nillable=False)
    # class Attributes(ComplexModel.Attributes):
    #     min_occurs=1
    #     nillable=True

class sendMessageFault1_sendMessageFault(ErrorInfo):
    _type_name__="sendMessageFault1_sendMessageFault"

class sendDeliveryNotificationFault1_sendDeliveryNotificationFault(ErrorInfo):
    __type_name__="sendDeliveryNotificationFault1_sendDeliveryNotificationFault"
