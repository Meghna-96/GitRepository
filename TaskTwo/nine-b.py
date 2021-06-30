x = 35
while True:
  guess = input('Please guess the lucky number: ')
  if int(guess)!=x:
    ans = input('Incorrect! Would you like to guess again?')
    if ans.lower()=='yes':
      print('Okay!')
    elif ans.lower()=='no':
      print("Alright! Maybe next time!")
      break
  else:
    print("You guessed it!")
    break
