def foo():
  try:
    return 1
  finally:
    return 2
  
k = foo()
print(k)


#2

def a():
  try:
    f(x, 4)
  finally:
    print('after f')
    print('after f?')
a()

# after f
# after f?
# NameError                                 Traceback (most recent call last)
# <ipython-input-32-a3d3b56d886e> in <module>()
#       5     print('after f')
#       6     print('after f?')
# ----> 7 a()

# <ipython-input-32-a3d3b56d886e> in a()
#       1 def a():
#       2   try:
# ----> 3     f(x, 4)
#       4   finally:
#       5     print('after f')

# NameError: name 'f' is not defined
