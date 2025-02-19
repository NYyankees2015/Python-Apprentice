# Demonstrate function arguments

def greet_user(name, greeting):
    print(f"{greeting}, {name}!")
9 m
# Call function with "positional" arguments. He first argument
# is assigned `name`, the second is assigned `greeting`.

greet_user("Alice", "Bounjour")

# We can also call the function with "keyword" arguments. This
# allows us to specify the arguments in any order.

greet_user(greeting="Hello", name="Alice") # greeting and name are in opposite order!

# You can mix positional and keyword arguments, but all positional
# arguments must come first.

greet_user("Bob", greeting="Hello")


# You can't have a positional argument after a keyword argument.
# This will cause an error ( uncomment and run to see )
# greet_user(name = "Bob", greeting)

# You also can't specify an argument more than once. This will also
# cause an error ( uncomment and run to see )
# greet_user("Bob", name="Bob")


# And, you can't skip an argument ( if it doesn't have a default value.)
# This will also cause an error ( uncomment and run to see )
# greet_user("Bob"



































































































