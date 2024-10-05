class Human:
  def __init__(self, name):
      self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers != []:
            print(f"В автомобілі {self.brand} ssdsdsddds:")
            for passenger in self.passebgers:
                print(passenger.name)
        else:
            print(f"sdsdadsdsafaf {self.brand} ddfdgdggd!:")

h1 = Human(input("dfjdfdfldfhflff: " ))
h2 = Human("vetal")

car1 = Auto ("Mercedes")
car1.add_passengers(h1,h2)
car1.print_passengers_names()