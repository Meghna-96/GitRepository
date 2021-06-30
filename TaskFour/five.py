def uppercase(input_string):
  out = input_string.split(' ')
  result = []
  for i in out:
    result.append(i.upper())
  return ' '.join(result)

uppercase('Hello world Practice makes man perfect')
