# This is a single-line comment
name = "Tapan"  # This is an inline comment
print(name)

# This is a multi-line comment
# spread across several lines
# to explain something in detail.
age = 40
print(age)

"""
This is also used as a multi-line comment
using triple quotes.
It is not assigned to any variable,
so Python ignores it at runtime.
"""


def greet(name: str) -> str:
    """
    This function takes a name as input
    and returns a greeting message.

    Parameters:
        name (str): The name of the person

    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"

print(greet("Tapan"))
