String = 'Consultadd Training'
def gen_reverse(string):
  for i in range(len(string)-1,-1,-1):
    yield string[i]

rev_string = gen_reverse(String)
for i in rev_string:
  print(i, end="")
