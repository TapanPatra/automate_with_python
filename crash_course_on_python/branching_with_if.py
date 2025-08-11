# Function to check username validity
def check_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters")
    else:
        print("Valid username")


# Function to check if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    return False


# Example usage
check_username("Al")    # Invalid username
check_username("Alex")  # Valid username

print(is_even(4))  # True
print(is_even(7))  # False


# Function to check username validity using elif
def check_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters.")
    elif len(username) > 15:
        print("Invalid username. Must not exceed 15 characters.")
    else:
        print("Valid username")


# Example usage
check_username("Al")                  # Too short
check_username("Alex")                # Valid
check_username("SuperLongUserNameHere")  # Too long

