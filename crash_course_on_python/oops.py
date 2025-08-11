# Creating Instance of Class
class Apple:
    def __init__(self, colour, flavour):
        self.colour = colour
        self.flavour = flavour
    def __str__(self):
        return "an apple which is {} and {}".format(self.colour, self.flavour)
    
honeyCrisp = Apple("red", "sweet")
print(honeyCrisp) # an apple which is red and sweet

# Performing Special Operation - Denuder Method
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def __add__(self, other):
        return self.area() + other.area()
    
print("The area of both Triangle is ", Triangle(10,5) + Triangle(6,8)) # The area of both Triangle is  49.0

# Instance Methods and Instance Variable
class Piglet:
    name = "Piglet"
    years = 0
    def speak(self):
        print("Oink! I am {}! oink! ".format(self.name))
    
    def pigYears(self):
        return self.years*18
    
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak() # Oink! I am Hamlet! oink!

piggy = Piglet()
piggy.years = 2
print(piggy.pigYears()) # 36



        
