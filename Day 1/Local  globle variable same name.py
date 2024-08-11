variable = "global"

def example_function():
    variable = "local"
    print("Inside the function:", variable)

example_function()

print("Outside the function:", variable)