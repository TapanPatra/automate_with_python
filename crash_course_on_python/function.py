# Define Function - Function return nothing
def greeting(name):
    print("Welcome " + name)

greeting("Tapan") # Welcome Tapan

# function returning values
def areaOfTriangle(base, height):
    return base * height / 2
area_a = areaOfTriangle(5,4)
print("The area of triangle is " + str(area_a)) # The area of triangle is 10.0

# More than one return values
def convert_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - hours * 3600)//60
    remaining_seconds = seconds - hours * 3600 - minutes*60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds) # 1 23 20





