a = input('Please Enter a value: ')

def lowerCamelCase(string_input):
  res = string_input.split()
  s = "".join(word[0].upper() + word[1:].lower() for word in res)
  return s[0].lower() + s[1:]
 
def UpperCamelCase(string_input):
  res = string_input.split()
  s = "".join(word[0].upper() + word[1:].lower() for word in res)
  return s[0].upper() + s[1:]

def snakeCase(string_input):
  res = string_input.split()
  s = "_".join(word[:].lower() for word in res)
  return s

def Uppercase(string_input):
  s = string_input.upper()
  return s 

print(lowerCamelCase(a))
print(UpperCamelCase(a))
print(snakeCase(a))
print(Uppercase(a))
