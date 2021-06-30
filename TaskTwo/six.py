x = 123
for i in x:
  print(i)

# TypeError                                 Traceback (most recent call last)
# <ipython-input-9-01bc6a8900bc> in <module>()
#       1 x = 123
# ----> 2 for i in x:
#       3   print(i)

# TypeError: 'int' object is not iterable

i = 0
while (i<5):
  print(i)
  i+=1
  if(i==3):
    break
  else:
    print("error")
    
    
# 0
# error
# 1
# error
# 2

count = 0
while True:
  print(count)
  count+=1
  if count >= 5:
    break
    
# 0
# 1
# 2
# 3
# 4
