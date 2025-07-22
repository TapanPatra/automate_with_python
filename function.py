def add(a, b):
    return a + b

print(add(3, 4))  # 7
def greet(name):
    print("Hello", name)

greet("Tapan")

def square_and_cube(n):
    return n**2, n**3

sq, cube = square_and_cube(3)
print(sq, cube)  # 9 27

for i in range(3):
    print(i)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
