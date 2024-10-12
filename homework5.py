class Animal:
 def __init__(self):
  self.name = "Animal"

class Fly(Animal):
 def __init__(self):
        self.name = "Fly"

class butterfly(Animal):
    def __init__(self):
        self.name = "butterfly"

print(issubclass(Animal, Fly))
print(issubclass(Animal, butterfly))