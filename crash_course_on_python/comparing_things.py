# Comparison operators example

a = 10
b = 20

# Equal to
print(f"{a} == {b} :", a == b) # 10 == 20 : False

# Not equal to
print(f"{a} != {b} :", a != b) # 10 != 20 : True

# Greater than
print(f"{a} > {b}  :", a > b) # 10 > 20  : False

# Less than
print(f"{a} < {b}  :", a < b) # 10 < 20  : True

# Greater than or equal to
print(f"{a} >= {b} :", a >= b) # 10 >= 20 : False

# Less than or equal to
print(f"{a} <= {b} :", a <= b) # 10 <= 20 : True

# Comparing strings
str1 = "apple"
str2 = "banana"
# alphabetical order
print(f'"{str1}" < "{str2}" :', str1 < str2)  # "apple" < "banana" : True



# Comparing lists
list1 = [1, 2, 3]
list2 = [1, 2, 4]
# compares element by element 
print("list1 == list2 :", list1 == list2) # list1 == list2 : False
print("list1 < list2  :", list1 < list2)  # list1 < list2  : True

