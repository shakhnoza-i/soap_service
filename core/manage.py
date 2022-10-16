#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import spyne.const
from spyne.interface.wsdl import Wsdl11
from spyne.interface.xml_schema._base import XmlSchema

from wsdl_app.patched_wsdl import add_message_for_object, add_port_type, add_bindings_for_methods


spyne.const.DEFAULT_DECLARE_ORDER = 'declared'

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
    Wsdl11.add_port_type = add_port_type
    Wsdl11.add_bindings_for_methods = add_bindings_for_methods
    main()
