# String basics
name = "Jaylon"

# Concatenation
full_name = name + " Smith"
print(full_name)

# Multiplication
print("example" * 3)  # exampleexampleexample

# Length of string
print(len(name))  # 6

# String indexing
print(name[0])   # J
print(name[-1])  # n

# String slicing
print(name[1:4])   # ayl
print(name[:4])    # Jayl
print(name[2:])    # ylon


# Example: IndexError
# Accessing index out of range
pets = "Cats & Dogs"
# print(pets[20])  # Uncomment to see: IndexError: string index out of range

# Strings are immutable
message = "A Kong string"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

# Index method
pets = "Cats & Dogs"
print(pets.index("a"))      # 1
print(pets.index("Dogs"))   # 7

# ValueError when substring not found
# print(pets.index("Dragons"))  # Uncomment to see: ValueError

# Membership operator
print("Cats" in pets)      # True
print("Dragons" in pets)   # False

# Replace domain function
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

# Example usage
print(replace_domain("user@old.com", "old.com", "new.com"))


# More String Methods
print("Mountains".upper())  # MOUNTAINS
print("Mountains".lower())  # mountains

# Strip whitespace
print("  Yes ".strip())   # "Yes"
print("  Yes ".lstrip())  # "Yes "
print("  Yes ".rstrip())  # "  Yes"

# Count occurrences
print("The number of times e occurs in the string".count("e"))  # 5

# Endswith
print("forest".endswith("t"))  # True

# Alphanumeric check
print("forest".isnumeric())    # False

# Join example
words = ["This", "is", "a", "phrase", "joined", "by", "spaces"]
print(" ".join(words))  # "This is a phrase joined by spaces"

# Split example
print("This is another example".split())  
# ['This', 'is', 'another', 'example']

# Advanced String Methods - Formatting
name = "Mary"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

print("Your lucky number is {number}, {name}"
      .format(name=name, number=len(name) * 3))

price = 7.25
print("Base price: ${:.2f}".format(price))
