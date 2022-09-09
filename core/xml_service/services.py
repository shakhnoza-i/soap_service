from bs4 import BeautifulSoup
from django.template.loader import render_to_string
from .serializers import AddSerializer


# root = """
# <?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <Add xmlns="http://tempuri.org/">
#       <intA>8</intA>
#       <intB>15</intB>
#     </Add>
#   </soap:Body>
# </soap:Envelope>
# """


def format_xml(data):
  root = data
  login_page = root.encode('utf-8')
  soup = BeautifulSoup(login_page)
  int_a = int(soup.find('inta').text)
  int_b = int(soup.find('intb').text)
  int_c = int_a + int_b
  return render_to_string("add_response.xml", {"int_c": int_c,})
