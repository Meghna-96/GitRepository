def filter_even(number):
    if(number%2==0):
        return True
    else:
        return False
  
even_numbers=filter(filter_even, range(1,21))
print(list(even_numbers))
