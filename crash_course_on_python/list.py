# List examples
x = ["Now", "we", "are", "cooking"]

# Length of list
print(len(x))  # 4

# Membership test
print("are" in x)  # True

# Type check
print(type(x))  # <class 'list'>

# Indexing
print(x[3])  # cooking

# Slicing
print(x[1:3])  # ['we', 'are']

# Looping through a sequence
for element in x:
    print(element)

# Modifying the content of a list (lists are mutable)
fruits = ["Pineapple", "Banana", "Apple", "Melon"]

# Append to the end
fruits.append("Kiwi")

# Insert at specific index
fruits.insert(0, "Orange")

# Remove an item by value
fruits.remove("Melon")  # If "Melon" not in list → ValueError

# Remove by index and return it
removed_fruit = fruits.pop(3)

print(fruits)
print("Removed fruit:", removed_fruit)
