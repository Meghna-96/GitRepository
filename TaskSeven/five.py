class Person:

  def __init__(self, age):
    self.age = age

    if self.age < 0:
      self.age = 0
      print('Age is not valid, setting age to 0')

  
  def yearPasses(self, no_of_years):
    self.age += no_of_years
    print('Age is:', self.age)


  def amIOld(self):
    if (self.age<13):
      print('You are young!')
    elif (self.age >=13 and self.age <=19):
      print('You are a teenager!')
    else:
      print('You are old!')

a = Person(12)
b = Person(24)
c = Person(38)




l = [-1,4,10,16,18,64,38]
for i in l:
  obj = Person(i)
  obj.amIOld()
