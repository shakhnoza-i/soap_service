from email import message
from spyne.model.primitive import Unicode
from spyne.model.complex import ComplexModelBase, ComplexModel, ComplexModelMeta
from spyne.model.fault import Fault


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
    # __type_name__ = "Fault"
    __name__="getMessagesFault1_getMessagesFault"
    class Attributes(ComplexModel.Attributes):
        min_occurs=1
        nillable=True
