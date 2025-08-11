# Logical operators example

a = True
b = False

# AND - True if both are True
print("a and b:", a and b)   # False

# OR - True if at least one is True
print("a or b :", a or b)    # True

# NOT - Inverts the boolean value
print("not a  :", not a)     # False
print("not b  :", not b)     # True

# Using with comparisons
x = 10
y = 20

print("(x > 5) and (y > 15):", (x > 5) and (y > 15))   # True and True → True
print("(x > 15) or (y > 15):", (x > 15) or (y > 15))   # False or True → True
print("not (x == 10):", not (x == 10))                 # not True → False
