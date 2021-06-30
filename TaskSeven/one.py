import math
d = input('Enter values:').split(',')
c, h = 50, 30

for i in d:
  q = math.sqrt((2*c*int(i))/h)
  print(q)
