x = 24
while True:
  guess = input('Please guess the lucky number: ')
  if int(guess)!=x:
    print('Keep guessing')
  else:
    break
print("You guessed it!")
