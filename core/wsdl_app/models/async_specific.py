from spyne.model.primitive import Unicode, DateTime
from spyne.model.complex import ComplexModel, Array
from spyne.model.enum import Enum

from .common import SenderInfo, Property, guid


class AsyncMessageInfo(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/AsyncChannel/v10/ITypes'
    messageId = Unicode(doc='Идентификатор сообщения. Генерируется ШЭП', min_occurs=0)
    correlationId = Unicode(doc='Идентификатор цепочки сообщений. Генерируется ШЭП', min_occurs=0)
    serviceId = Unicode(doc='Идентификатор взаимодействия. По реестру сервисов ШЭП.', min_occurs=1)
    messageType = Enum('REQUEST', 'NOTIFICATION', 'UPDATE', 'RESPONSE', min_occurs=1, type_name='messageType')
    routeId = Unicode(doc='Идентификатор маршрута', min_occurs=0)
    messageDate = DateTime(doc='Дата создания сообщения', min_occurs=1)
    sender = SenderInfo
    properties = Property # Массив дополнительных свойств сообщения
    sessionId = guid
