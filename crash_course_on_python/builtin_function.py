# Built-in functions example

# Sample data
numbers = [5, 12, 3, 9, 21]
name = "Tapan"

# print() - Display output
print("Name:", name) # Name: Tapan
print("Numbers:", numbers) # Numbers: [5, 12, 3, 9, 21]

# type() - Get the data type
print("Type of name:", type(name)) # Type of name: <class 'str'>
print("Type of numbers:", type(numbers)) # Type of numbers: <class 'list'>

# str() - Convert to string
age = 40
age_str = str(age)
print("Age as string:", age_str, "Type:", type(age_str)) # Age as string: 40 Type: <class 'str'>

# max() - Get largest value
print("Max number:", max(numbers)) # Max number: 21

# min() - Get smallest value
print("Min number:", min(numbers)) # Min number: 3

# sorted() - Sort list (ascending and descending)
print("Numbers sorted ascending:", sorted(numbers)) # Numbers sorted ascending: [3, 5, 9, 12, 21]
print("Numbers sorted descending:", sorted(numbers, reverse=True)) # Numbers sorted descending: [21, 12, 9, 5, 3]

# len() - Get number of elements
print("Length of name:", len(name)) # Length of name: 5
print("Number of items in numbers:", len(numbers)) # Number of items in numbers: 5
