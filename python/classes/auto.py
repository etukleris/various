class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    return "This is a %s %s with %s MPG." % (self.color,self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)

#print (my_car.display_car())
#while True:
model = input("Car model?")
color = input("Car color?")
mpg   = int(input("MPG?"))
new_car = Car(model,color,mpg)
print (new_car.display_car())
