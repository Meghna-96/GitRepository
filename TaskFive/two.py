import sys
try:
  with open(sys.argv[1], 'r') as my_file:
    print(my_file.read())
except OSError as err:
  print('Incorrect file name. Please enter name again!', err)
