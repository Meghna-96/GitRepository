def filter_multiples(number):
    if(number%3!=0 and number%7==0):
        return True
    else:
        return False

result = filter(filter_multiples,range(2000, 3201))
print(list(result))  
