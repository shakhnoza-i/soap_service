from spyne.model.primitive import Unicode
from spyne.model.complex import ComplexModelBase, ComplexModel


class EmailString(Unicode):
    __type_name__ = 'EmailString'

    class Attributes(Unicode.Attributes):
        max_length = 128
        pattern = '[^@]+@[^@]+'


class AsyncSendMessage(ComplexModel):
    __type_name__ = 'bons3:AsyncSendMessageRequest'
    class Attributes(ComplexModel.Attributes):
        declare_order = 'declared'
