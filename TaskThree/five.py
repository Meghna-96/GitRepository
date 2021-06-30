predefined_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in predefined_list:
  if(i%2 != 0 or i ==0 ):
    new_list.append(i)
print(new_list)
