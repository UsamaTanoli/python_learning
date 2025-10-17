import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end - start} time")
#         return result
#     return wrapper

# @timer
# def sleeper(n):
#     time.sleep(n)

# sleeper(2)
# sleeper(3)

# def decorator(func):
#     def wrapper():
# #         print("start")
# #         func()
# #         print("end")
# #     return wrapper


# # @decorator
# # def say_hello():
# #     print("hello")

# # say_hello()

# say_hello = decorator(say_hello)
# say_hello()


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("start")
#         func(*args, **kwargs)
#         print("end")
#     return wrapper


# @my_decorator
# def greet(name, cast, habit):
#     print(f"Hello, {name} {cast}! your habit is {habit}")

# greet("Shaban", "Tanoli", "Susti")

# def outer_function():
#     message = "Hello from the outer function!"

#     def inner_function():
#         print(message)  # Access the variable from the outer function

#     return inner_function  # Return the inner function

# my_func = outer_function()  # my_func now points to inner_function
# my_func()  # This calls i