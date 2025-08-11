# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x * x for x in numbers]
print(squared_numbers)


# List comprehension example
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)

# Same thing with list comprehension
multiples = [x * 7 for x in range(1, 11)]
print(multiples)

# List comprehension with condition
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

# List operations and methods
sequence = [10, 20, 30, 40, 50]
print(len(sequence))      # Length of list
print(sequence[0])        # Access first element
print(sequence[:3])       # Slicing

for index, element in enumerate(sequence):
    print(index, element)

# Modifying lists
fruits = ["Pineapple", "Banana", "Apple", "Melon"]

fruits[2] = "Strawberry"       # Replace
fruits.append("Kiwi")          # Add to end
fruits.insert(0, "Orange")     # Insert at position
fruits.pop(1)                  # Remove by index
fruits.remove("Melon")         # Remove by value
fruits.reverse()               # Reverse list
copy_fruits = fruits.copy()    # Copy list
fruits.extend(["Mango", "Papaya"])  # Extend list

print(fruits)

# map() example: apply function to each element
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# zip() example: combine lists into tuples
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
paired = list(zip(names, scores))
print(paired)
