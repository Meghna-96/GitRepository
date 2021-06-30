result=[]
for i in range(1,6):
  result.append(i*i)
  result.append((31-i)*(31-i))

print(sorted(result))
