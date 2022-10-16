from spyne.model.primitive import Unicode, DateTime
from spyne.model.fault import Fault
from spyne.model.complex import ComplexModel, XmlAttribute, XmlAttributeRef



guid = Unicode(doc = 'Идентификатор сессии', min_occurs=0, type_name = 'guid',
               pattern = '\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}',
               __namespace__ = 'http://bip.bee.kz/common/v10/Types')


class ErrorInfo(Fault):
    __namespace__ = 'http://bip.bee.kz/common/v10/Types'
    errorCode = Unicode(doc='Код ошибки', min_occurs=1)
    errorMessage = Unicode(doc = 'Сообщение ошибки', min_occurs=1)
    errorData = Unicode(doc = 'Дополнительное описание ошибки', min_occurs=0)
    errorDate = DateTime(doc = 'Дата ошибки', min_occurs=1)
    subError = Unicode(doc = 'Дочерняя ошибка', min_occurs=0, type_name = 'ErrorInfo') # type="bons1:ErrorInfo"
    sessionId = guid


class MessageData(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/common/v10/Types'
    data = Unicode(doc='Объект бизнес-данные сообщения', min_occurs=1)
    class Attributes(ComplexModel.Attributes):
        min_occurs=1


class SenderInfo(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/common/v10/Types'
    senderId = Unicode(doc='Идентификатор отправителя (системы отправителя)', min_occurs=1)
    password = Unicode(doc='Пароль отправителя', min_occurs=0)


class Property(ComplexModel):
    __namespace__ = 'http://bip.bee.kz/common/v10/Types'
    key = Unicode(doc='Ключ своиства', min_len=0, max_len=30, min_occurs=1)
    value = Unicode(doc='Значение своиства', min_len=0, max_len=500, min_occurs=1)
    
