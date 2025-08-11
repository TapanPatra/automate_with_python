# Example: Counting from 1 to 5 using while loop

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Increment to avoid infinite loop

print("Loop finished!")

# This loop will run forever
'''
while True:
    print("This will keep printing endlessly...")
'''

# Another example with a logic mistake causing an infinite loop
'''
count = 1
while count > 0:  # This is always true because count is increasing
    print(count)
    count += 1
'''

#  use break to exit a while loop
count = 1

while True:  # Infinite loop
    print("Count:", count)
    count += 1
    
    if count > 5:  # Exit condition
        break  # Stops the loop

print("Loop ended.")


# While loop (index)
greeting = "Hello"
index = 0
while index < len(greeting):
    print(greeting[index])
    index += 1

# While loop slicing
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1