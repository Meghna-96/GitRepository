def upper_lower(string):
  upper, lower = 0,0
  for ch in string:
    if ch.islower():
      lower+=1
    else:
      upper+=1
  print('No. of Uppercase Characters:', upper)
  print('No. of Lowercase Characters:', lower)

upper_lower('abcSdefPghijQkl')
