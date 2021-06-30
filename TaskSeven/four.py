class Time(object):

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins

  def addTime(obj1, obj2):
    new_time = Time(0,0)
    if (obj1.mins+obj2.mins > 60):
      new_time.hours = (obj1.mins+obj2.mins)//60
    new_time.hours = new_time.hours+obj1.hours+obj2.hours
    new_time.mins = (obj1.mins+obj2.mins)-(((obj1.mins+obj2.mins)//60)*60)
    return new_time

  def displayTime(self):
    print ('Time is',self.hours,'hours and',self.mins,'minutes.')


  def displayMinute(self):
    print ((self.hours*60)+self.mins)


a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
