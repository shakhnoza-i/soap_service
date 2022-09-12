from django.template.loader import render_to_string


def format_xml(data):
  root = data['{http://schemas.xmlsoap.org/soap/envelope/}Body']

  math_oper = str(root).split(':')[1].split('}')[-1][0:-1]
  # breakpoint()
  if math_oper == 'Add':
    lev1 = root['{http://tempuri.org/}Add']
  elif math_oper == 'Subtract':
    lev1 = root['{http://tempuri.org/}Subtract']
  elif math_oper == 'Multiply':
    lev1 = root['{http://tempuri.org/}Multiply']
  else:
    lev1 = root['{http://tempuri.org/}Divide']

  int_a = lev1['{http://tempuri.org/}intA']
  int_b = lev1['{http://tempuri.org/}intB']

  if math_oper == 'Add':
    int_c = int_a + int_b
    return render_to_string("add_response.xml", {"int_c": int_c,})
  elif math_oper == 'Subtract':
    int_c = int_a - int_b
    return render_to_string("subtract_response.xml", {"int_c": int_c,})
  elif math_oper == 'Multiply':
    int_c = int_a * int_b
    return render_to_string("multiply_response.xml", {"int_c": int_c,})
  else:
    int_c = int_a / int_b
    return render_to_string("divide_response.xml", {"int_c": int_c,})
