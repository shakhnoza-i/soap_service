#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from spyne.interface.wsdl import Wsdl11
from spyne.interface.wsdl.wsdl11 import check_method_port
from lxml.etree import SubElement
from lxml.builder import E
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


def add_port_type(self, service, root, service_name, types, url):
    # FIXME: I don't think this call is working.
    cb_port_type = self._add_callbacks(service, root, types,
                                                            service_name, url)
    applied_service_name = self._get_applied_service_name(service)

    port_binding_names = []
    port_type_list = service.get_port_types()
    if len(port_type_list) > 0:
        for port_type_name in port_type_list:
            port_type = self._get_or_create_port_type(port_type_name)
            port_type.set('name', port_type_name)

            binding_name = self._get_binding_name(port_type_name)
            port_binding_names.append((port_type_name, binding_name))

    else:
        port_type = self._get_or_create_port_type(service_name)
        port_type.set('name', service_name)

        binding_name = self._get_binding_name(service_name)
        port_binding_names.append((service_name, binding_name))

    for method in service.public_methods.values():
        check_method_port(service, method)

        if method.is_callback:
            operation = SubElement(cb_port_type, WSDL11("operation"))
        else:
            operation = SubElement(port_type, WSDL11("operation"))

        operation.set('name', method.operation_name)

        if method.doc is not None:
            operation.append(E(WSDL11("documentation"), method.doc))

        operation.set('parameterOrder', method.in_message.get_element_name())

        op_input = SubElement(operation, WSDL11("input"))
        op_input.set('name', method.in_message.get_element_name() + 'Request')
        op_input.set('message',
                        method.in_message.get_element_name_ns(self.interface) + 'RequestMsg')

        if (not method.is_callback) and (not method.is_async):
            op_output = SubElement(operation, WSDL11("output"))
            op_output.set('name', method.out_message.get_element_name())
            op_output.set('message', method.out_message.get_element_name_ns(
                                                            self.interface) + 'Msg')

            if not (method.faults is None):
                for f in method.faults:
                    fault = SubElement(operation, WSDL11("fault"))
                    fault.set('name',  method.in_message.get_element_name() + 'Fault')
                    fault.set('message', '%s:%s' % (
                                    f.get_namespace_prefix(self.interface),
                                    f"{method.in_message.get_element_name()}_{method.in_message.get_element_name()}FaultMsg"))

    ser = self.service_elt_dict[applied_service_name]
    import pdb
    pdb.set_trace()
    for port_name, binding_name in port_binding_names:
        self._add_port_to_service(ser, port_name, binding_name)




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
    main()
