from ast import literal_eval

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str
a = input('Please Enter a value: ')
dt = get_type(a)
print('The data type of the input value is', str(dt)[8:-2])
