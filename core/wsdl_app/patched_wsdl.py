from lxml import etree
from lxml.etree import SubElement
from lxml.builder import E
import spyne.const.xml as ns
from spyne.const.xml import WSDL11
from spyne.interface.wsdl.wsdl11 import check_method_port, _in_header_msg_suffix, _out_header_msg_suffix


def add_message_for_object(self, root, messages, obj, message_name):
    if obj is not None and not (message_name in messages):
        messages.add(message_name)

        message = SubElement(root, WSDL11("message"))
        if (message_name.endswith('Response')):
            message.set('name', message_name + 'Msg')
        elif (message_name.endswith('Fault')):
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
            elif (message_name.endswith('Fault')):
                part.set('name', message_name)
# part.set('element', f"{message_name}1_{message_name}") # can't override it - it must match with <xsd:element name="sendMessageFault1_sendMessageFault"
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
    for port_name, binding_name in port_binding_names:
        self._add_port_to_service(ser, port_name, binding_name)


def add_bindings_for_methods(self, service, root, service_name,
                                    cb_binding):

    pref_tns = self.interface.get_namespace_prefix(self.interface.get_tns())
    input_binding_ns = ns.get_binding_ns(self.interface.app.in_protocol.type)
    output_binding_ns = ns.get_binding_ns(self.interface.app.out_protocol.type)

    def inner(method, binding):
        operation = etree.Element(WSDL11("operation"))
        operation.set('name', method.operation_name)

        soap_operation = SubElement(operation, input_binding_ns("operation"))
        soap_operation.set('soapAction', '')

        # get input
        input = SubElement(operation, WSDL11("input"))
        input.set('name', method.in_message.get_element_name() + 'Request')

        soap_body = SubElement(input, input_binding_ns("body"))
        soap_body.set('use', 'literal')

        # get input soap header
        in_header = method.in_header
        if in_header is None:
            in_header = service.__in_header__

        if not (in_header is None):
            if isinstance(in_header, (list, tuple)):
                in_headers = in_header
            else:
                in_headers = (in_header,)

            if len(in_headers) > 1:
                in_header_message_name = ''.join((method.name,
                                                    _in_header_msg_suffix))
            else:
                in_header_message_name = in_headers[0].get_type_name()

            for header in in_headers:
                soap_header = SubElement(input, input_binding_ns('header'))
                soap_header.set('use', 'literal')
                soap_header.set('message', '%s:%s' % (
                            header.get_namespace_prefix(self.interface),
                            in_header_message_name))
                soap_header.set('part', header.get_type_name())

        if not (method.is_async or method.is_callback):
            output = SubElement(operation, WSDL11("output"))
            output.set('name', method.out_message.get_element_name())

            soap_body = SubElement(output, output_binding_ns("body"))
            soap_body.set('use', 'literal')

            # get output soap header
            out_header = method.out_header
            if out_header is None:
                out_header = service.__out_header__

            if not (out_header is None):
                if isinstance(out_header, (list, tuple)):
                    out_headers = out_header
                else:
                    out_headers = (out_header,)

                if len(out_headers) > 1:
                    out_header_message_name = ''.join((method.name,
                                                    _out_header_msg_suffix))
                else:
                    out_header_message_name = out_headers[0].get_type_name()

                for header in out_headers:
                    soap_header = SubElement(output, output_binding_ns("header"))
                    soap_header.set('use', 'literal')
                    soap_header.set('message', '%s:%s' % (
                            header.get_namespace_prefix(self.interface),
                            out_header_message_name))
                    soap_header.set('part', header.get_type_name())

            if not (method.faults is None):
                for f in method.faults:
                    wsdl_fault = SubElement(operation, WSDL11("fault"))
                    # wsdl_fault.set('name', f.get_type_name())
                    wsdl_fault.set('name', method.in_message.get_element_name() + 'Fault')

                    soap_fault = SubElement(wsdl_fault, input_binding_ns("fault"))
                    # soap_fault.set('name', f.get_type_name())
                    soap_fault.set('name', method.in_message.get_element_name() + 'Fault')
                    soap_fault.set('use', 'literal')

        if method.is_callback:
            relates_to = SubElement(input, input_binding_ns("header"))

            relates_to.set('message', '%s:RelatesToHeader' % pref_tns)
            relates_to.set('part', 'RelatesTo')
            relates_to.set('use', 'literal')

            cb_binding.append(operation)

        else:
            if method.is_async:
                rt_header = SubElement(input, input_binding_ns("header"))
                rt_header.set('message', '%s:ReplyToHeader' % pref_tns)
                rt_header.set('part', 'ReplyTo')
                rt_header.set('use', 'literal')

                mid_header = SubElement(input, input_binding_ns("header"))
                mid_header.set('message', '%s:MessageIDHeader' % pref_tns)
                mid_header.set('part', 'MessageID')
                mid_header.set('use', 'literal')

            binding.append(operation)

    port_type_list = service.get_port_types()
    if len(port_type_list) > 0:
        for port_type_name in port_type_list:

            # create binding nodes
            binding = SubElement(root, WSDL11("binding"))
            binding.set('name', self._get_binding_name(port_type_name))
            binding.set('type', '%s:%s'% (pref_tns, port_type_name))

            transport = SubElement(binding, input_binding_ns("binding"))
            transport.set('style', 'document')
            transport.set('transport', self.interface.app.transport)

            for m in service.public_methods.values():
                if m.port_type == port_type_name:
                    inner(m, binding)

    else:
        # here is the default port.
        if cb_binding is None:
            cb_binding = SubElement(root, WSDL11("binding"))
            cb_binding.set('name', service_name)
            cb_binding.set('type', '%s:%s'% (pref_tns, service_name))

            transport = SubElement(cb_binding, input_binding_ns("binding"))
            transport.set('style', 'document')
            transport.set('transport', self.interface.app.transport)

        for m in service.public_methods.values():
            inner(m, cb_binding)

    return cb_binding
