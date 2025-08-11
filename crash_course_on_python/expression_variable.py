# ---- Variables and Data Types ----
age = 25                # int
height = 5.9            # float
name = "Tapan"          # string
is_active = True        # bool

print("Name:", name, "Type:", type(name)) # Name: Tapan Type: <class 'str'>
print("Age:", age, "Type:", type(age)) # Age: 25 Type: <class 'int'>
print("Height:", height, "Type:", type(height)) # Height: 5.9 Type: <class 'float'>
print("Active:", is_active, "Type:", type(is_active)) # Active: True Type: <class 'bool'>

# ---- Explicit Type Conversion (Casting) ----
# Convert int to float
age_float = float(age)
print("Explicit conversion int -> float:", age_float, type(age_float)) # Explicit conversion int -> float: 25.0 <class 'float'>

# Convert float to int
height_int = int(height)
print("Explicit conversion float -> int:", height_int, type(height_int)) # Explicit conversion float -> int: 5 <class 'int'>

# Convert int to string
age_str = str(age)
print("Explicit conversion int -> str:", age_str, type(age_str)) # Explicit conversion int -> str: 25 <class 'str'>

# ---- Implicit Type Conversion ----
# Python automatically converts int to float in expressions
result = age + height   # int + float → float
print("Implicit conversion result:", result, type(result)) #Implicit conversion result: 30.9 <class 'float'>

# ---- Another implicit example ----
x = 4  # int
y = 3.5  # float
sum_result = x + y
print(f"{x} + {y} = {sum_result} (Type: {type(sum_result)})") # 4 + 3.5 = 7.5 (Type: <class 'float'>)


# ---- Variable annotation ----
name: str = "Tapan"             # String type
scores: list[int] = [85, 90, 78]  # List of integers

print("Name:", name) # Name: Tapan
print("Scores:", scores) # Scores: [85, 90, 78]

# Loop through scores
for score in scores:
    print("Score:", score)
