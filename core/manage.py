#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from spyne.interface.wsdl import Wsdl11
from lxml.etree import SubElement
from spyne.const.xml import WSDL11


# spyne.const.DEFAULT_DECLARE_ORDER = 'declared'



def add_message_for_object(self, root, messages, obj, message_name):
    if obj is not None and not (message_name in messages):
        messages.add(message_name)

        message = SubElement(root, WSDL11("message"))
        if (message_name.endswith('Response')):
            message.set('name', message_name + 'Msg')
        else:
            message.set('name', message_name + 'RequestMsg')
        

        if isinstance(obj, (list, tuple)):
            objs = obj
        else:
            objs = (obj,)

        for obj in objs:
            part = SubElement(message, WSDL11("part"))
            if (message_name.endswith('Response')):
                part.set('name', message_name[:-8] + 'Result')
            else:
                part.set('name', message_name + 'Parameters')
        
            part.set('element', obj.get_element_name_ns(self.interface))



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    Wsdl11._add_message_for_object = add_message_for_object
    main()
