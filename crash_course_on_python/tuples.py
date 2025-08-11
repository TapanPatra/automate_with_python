# Example: Lists
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits[2] = "Strawberry"  # Change element at index 2
print(fruits)

# Tuples - sequence of elements of any type, immutable
fullname = ("Grace", "M", "Hopper")

# Tuple unpacking
first_name, middle_name, last_name = fullname
print(first_name)
print(middle_name)
print(last_name)

# Iterating over Lists and Tuples
winners = ["Ashley", "Dylan", "Reese"]

for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


# Tuples: Use Cases
# Protecting data - Immutable (cannot be changed)
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Convert list to tuple
print(my_tuple)

# Tuples with mutable objects
my_tuple = (1, 2, ['a', 'b', 'c'])

# my_tuple[0] = 3  # ❌ Raises TypeError: 'tuple' object does not support item assignment

# But mutable elements inside tuple can be changed
my_tuple[2][0] = 'x'
print(my_tuple)  # (1, 2, ['x', 'b', 'c'])

# Returning multiple values from a function
def calculate_numbers(a, b):
    return a + b, a - b, a * b, a / b

add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # 12
print(sub_result)  # 8
print(mul_result)  # 20
print(div_result)  # 5.0
