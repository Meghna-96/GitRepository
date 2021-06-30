def filter_even(number):
    if(number%2==0):
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8,9,10]
even_numbers=filter(filter_even, a)
sqaures = map(lambda x : x*x, even_numbers)
print(list(sqaures))
