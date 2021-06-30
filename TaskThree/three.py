sample_list = [23, 405, 40, 51, 45] #[]
if sample_list:
  sum = 0
  product = 1
  for i in sample_list:
    sum+=i
    product*=i
  print('Sum=', sum)
  print('Product=', product)
else:
  print('List does not exist')
