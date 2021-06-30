def decor_func(func):

  def wrapper_func(a,b):
    if (a < b):
      a,b = b,a
    return func(a,b)
  return wrapper_func

@decor_func
def simple_func(a,b):
  print(a - b)

simple_func(5,2)
simple_func(2,5)
# x = decor_func(simple_func)
# x(2,5)
