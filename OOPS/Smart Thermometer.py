

class Thermometer:
    def __init__(self,temp):
        self.temp=temp

    def get_fahrenheit(self):
        return f" the Fahernheit = {(self.temp*9/5)+32} "

    def set_temperature(self,new_temp):
        if(new_temp<-273.15):
            print(" the is not valid")
        else:
            self.temp=new_temp

obj=Thermometer(25)

print(" fahrenheit :- ",obj.get_fahrenheit())

obj.set_temperature(40)

print(" new value :- ",obj.get_fahrenheit())