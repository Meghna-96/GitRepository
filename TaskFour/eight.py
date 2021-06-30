def squares(a,b):
  lst=[]
  for i in range(a, b+1):
    lst.append(i*i)
  return tuple(lst)
squares(1,20)
