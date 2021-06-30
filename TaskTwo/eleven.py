x = 23
guesses = 0
while(guesses<5):
  guess = input('Please guess the lucky number: ')
  guesses+=1
  if int(guess)!=x:
    if (guesses!=5):
      print('Try Again! Number of remaining guesses:',5-guesses)
    else:
      print('Sorry but that was not very successful')
      break
  else:
    print("Good Guess!")
    break
print("Game Over!")
