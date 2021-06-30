def max_length(string1, string2):
  a = len(string1)
  b = len(string2)
  if (a>b):
    print(string1)
  elif (b>a):
    print(string2)
  elif (a==b):
    print(string1)
    print(string2)

max_length('Hello','Yellow')
