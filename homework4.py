class Artem:
  def __init__(self, name):
      self.name = name

class dumplinks:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers != []:
            print(f" food {self.brand} Artem:")
            for passenger in self.passebgers:
                print(passenger.name)
        else:
            print(f"dumplinks  {self.brand} batter!:")

d1 = dumplinks(input(": " ))
d2 = dumplinks("UwU")

Artem1 = dumplinks ("Acano")
Artem1.add_passengers(d1,d2)
Artem1.print_passengers_names()