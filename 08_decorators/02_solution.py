

def debug(func):
    def wrapper(*args, **kwargs):
        # Always join arguments, but if args/kwargs are empty, handle it later in the print statement
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        
        # Now handle the cases for printing
        if not args and not kwargs:
            # Case 1: No args and no kwargs
            print(f"calling: {func.__name__} with args 0 and kwargs 0")
        
        elif not args:
            # Case 2: No args, but kwargs present
            print(f"calling: {func.__name__} with args 0 and kwargs {kwargs_value}")
        
        elif not kwargs:
            # Case 3: Args present, but no kwargs
            print(f"calling: {func.__name__} with args {args_value} and kwargs 0")
        
        else:
            # Case 4: Both args and kwargs present
            print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        
        return func(*args, **kwargs)
    
    return wrapper

# Example functions
@debug
def print_hello():
    print("hello")

@debug
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")




@debug
def print_hello():
    print("hello")


@debug
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")


# Testing the functions
print_hello()

greet("usama", greeting="Hi")  # Explicit keyword argument for greeting
greet("usama", "Hi")  # Positional argument for greeting



@debug
def example_function(a=1, b=2):
    return a + b

# Test cases
example_function()                  # No args, no kwargs
example_function(3)                 # args present, no kwargs
example_function(b=4)               # no args, kwargs present
example_function(a=6, b=3)