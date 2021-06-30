with open('doc.txt', 'r') as my_file:
  x = my_file.readline()
  if len(x)%2==0:
    print(x)
