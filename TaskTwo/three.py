a, b, c = 20, 10, 30
avg = (a+b+c)/3
print('Avg', avg)
if (avg>a and avg>b and avg>c):
  print('Avg is greater than a,b,c')
else:
  if (avg>a and avg>b):
    print('Avg is higher than a, b')
  else:
    if (avg >a and avg>c):
      print('Avg is higher than a, c')
    else:
      if (avg>b and avg>c):
        print('Avg is higher than b, c')
      else:
        if (avg > a):
          print('Avg higher than only a')
        else:
          if (avg > b):
            print('Avg is higher than just b')
          else:
            if (avg > c):
              print('Avg is higher than just c')
