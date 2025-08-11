# Dictionary: pairs of keys and values
file_counts = {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

# Membership test
print('jpg' in file_counts)  # True

# Access value by key
print(file_counts['csv'])  # 2

# Set value when key exists
file_counts['csv'] = 17

# Add new key-value pair
file_counts['doc'] = 5

# Delete key-value pair
del file_counts['jpg']

# Iterating over dictionary
for extension in file_counts:  # keys
    print(extension)

for extension, amount in file_counts.items():  # key-value pairs
    print(extension, amount)

for value in file_counts.values():  # values only
    print(value)

# Letter counting program
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("banana"))  # {'b': 1, 'a': 3, 'n': 2}
