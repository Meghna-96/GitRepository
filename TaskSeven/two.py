class shape():

  def area(self):
    return 0

class square(shape):

  def __init__(self, length=0):
    self.length=length

  def area(self):
    return self.length*self.length

A = Square(5)
print(A.area())  
