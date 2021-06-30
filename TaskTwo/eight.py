string = input('Please enter a word: ')
digits=0
letters=0
for i in string:
  if (ord(i) in range(48, 57)):
    digits+=1
  else:
    letters+=1

print('Letters:', letters)
print('Digits:', digits)
