var = [b'class', b'function', b'method']

for line in var:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержимое переменной - {}\n'.format(line))
    print('длина переменной: {}\n'.format(len(line)))
