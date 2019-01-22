#filename:inherit-car1.py
#function: derived calss example using the car class
#class inheritance mechanism is :allowing multiple base classes,
#derived class can override any methods of its base class or classes
#The derived  method can call the method of a base class with the same name.

#program example is product production group for class regarding the car type

class PPG(object):
    car_status = "new"
    
    def __init__(self, model, color, year):
        print("PPG init")
        self.model = model
        self.color = color
        self.year   = year
        if year <= 2010:
           self.car_status = "used"
        else:
           print("new one")
           self.car_status = "new" 

    def display_ppg(self):
        return "This is a %s %s made on %s year " % (self.color, self.model, self.year)

    def drive_ppg(self):
        self.car_status = "used"


class ECar(PPG):
    def __init__(self, model, color, year, battery, price):
        print("\nECar init\t")
        PPG.__init__(self,model,color,year)
        self.battery = battery
        self.year   = year
        self.price   = price
#object.__repr__(self): called by the repr() built-in function and by string conversions (reverse quotes)
#to compute the "official" string representation of an object.
    def __repr__(self):
        return "<Car model:%s color:%s year:%s battery:%s price:%s  > " % (self.model, self.color,self.year, self.battery,self.price)

obj1 = PPG('Volvo', 'Blue', 1953)
print(obj1.display_ppg())
print("the car status is ", obj1.car_status)

e_carobj = ECar('Tesla ', 'Blue', 2014, 'Li-acid',200000)
print(e_carobj.display_ppg())

print(repr(e_carobj))
print("the car status is ", e_carobj.car_status)


