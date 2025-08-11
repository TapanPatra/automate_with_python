# for loop using range() in Python:
#######################################
# Print numbers from 0 to 4
for i in range(5):
    print(i)

'''
range() basics:

range(stop) → goes from 0 up to but not including stop.

range(start, stop) → goes from start to stop - 1.

range(start, stop, step) → goes from start to stop - 1 in increments of step.
'''
# 1 to 5
for i in range(1, 6):
    print(i)

# Even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)


# for loop iterating over a list
#######################################
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total += num

print("Sum:", total)

# Example of Nested loop 
#######################################
# Multiplication table (1 to 3)
for i in range(1, 4):        # Outer loop
    for j in range(1, 4):    # Inner loop
        print(f"{i} x {j} = {i * j}")
    print("---")  # Separator after each row

# Another Example of Nested Loop
#######################################
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# Strings in for loops
greeting = "Hello"
for c in greeting:
    print("The new character is:", c)