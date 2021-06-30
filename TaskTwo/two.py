calc = {1:'+', 2:'-', 3:'/' , 4:'*'}
print('Option 1 - Addition \nOption 2 - Subtraction \nOption 3 - Division \nOption 4 - Multiplication \nOption 5 - Average')
option = int(input('Choose one of the above Options:'))
num1, num2 = input('Now enter two numerical values:').split()
if option==5:
  first, second = input('Enter two more numerical values: ').split()
  result = (eval(num1+'+'+num2+'+'+first+'+'+second))/4
else:
  result = eval(num1+calc.get(option)+num2)

print('Negative' if result<0 else result)
