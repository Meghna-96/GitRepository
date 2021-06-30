#With third variable
a = 200
b = 500
print(a, b)
temp = a
a = b
b = temp
print(a, b)

#Without third variable
print(a, b)
a, b = b, a
print(a, b)
