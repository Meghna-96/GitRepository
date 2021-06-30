try:
  a = input('Please enter a number:')
  if(len(a)>4):
    print('The length is too short/long !!! Please provide only four digits')
    raise Exception
except:
  pass
