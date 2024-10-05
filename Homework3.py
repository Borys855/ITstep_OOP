class Pug:
  def __init__(self, name):
      self.name = name

class Food:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers != []:
            print(f" food {self.brand} pug:")
            for passenger in self.passebgers:
                print(passenger.name)
        else:
            print(f"food  {self.brand} ddfdgdggd!:")

p1 = Pug(input("dfjdfdfldfhflff: " ))
p2 = Pug("vetal")

car1 = Food ("Acano")
car1.add_passengers(p1,p2)
car1.print_passengers_names()