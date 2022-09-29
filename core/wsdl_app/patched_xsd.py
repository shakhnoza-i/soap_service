from lxml import etree
import spyne.const.xml as ns


def add_missing_elements_for_methods(self):
    def missing_methods():
        for service in self.interface.services:
            for method in service.public_methods.values():
                if method.aux is None:
                    yield method

    pref_tns = self.interface.prefmap[self.interface.tns]
    for method in missing_methods():
        elements = self.get_schema_info(pref_tns).elements
        try:
            i = elements.keys().index('ErrorInfo')
            elements[i].set('name', method)
        except ValueError:
            pass

    schema_root = self.schema_dict[pref_tns]
    for method in missing_methods():
        name = method.in_message.Attributes.sub_name
        if name is None:
            name = method.in_message.get_type_name()

        if not name in elements:
            element = etree.Element(ns.XSD('element'))
            element.set('name', name)
            element.set('type', method.in_message.get_type_name_ns(
                                                            self.interface))
            elements[name] = element
            schema_root.append(element)

        if method.out_message is not None:
            name = method.out_message.Attributes.sub_name
            if name is None:
                name = method.out_message.get_type_name()
            if not name in elements:
                element = etree.Element(ns.XSD('element'))
                element.set('name', name)
                element.set('type', method.out_message \
                                            .get_type_name_ns(self.interface))
                elements[name] = element
                schema_root.append(element)
                