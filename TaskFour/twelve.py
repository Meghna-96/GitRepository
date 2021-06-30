def div(a,b):
  try:
    return a/b
  except Exception as e:
    return 'Error:', e

div(5,0)
