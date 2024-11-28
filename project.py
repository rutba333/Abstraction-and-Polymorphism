#class 1
class BMW():
    def fuel_type(self):
        print("the fuel type of bmw is premium gasoline")

    def max_speed(self):
        print("The max speed of bmw is 250 kmph")

#class 1
class Ferrari():
    def fuel_type(self):
        print("the fuel type of ferrari is higher octane rating, ideally without ethanol")

    def max_speed(self):
        print("The max speed of ferrari is 249 miles per hour")

#object creation
obj_bmw=BMW()
obj_fera=Ferrari()

#common interface
for car in(obj_bmw,obj_fera):
   car.fuel_type()
   car.max_speed()


        
  