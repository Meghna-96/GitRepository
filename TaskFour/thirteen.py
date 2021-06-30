import functools
sample=[1,2,3,4,5,6,7]
reduced = functools.reduce(lambda x,y : int(str(x)+str(y)), sample)
print(reduced)
