# BASIC PROGRAM

# weather_types = input("Enter the current weather (sunny, cloudy, snowy, rainy): ").lower()

# if weather_types == "sunny":
#     output = "It's sunny, go for a walk!"
# elif weather_types == "cloudy":
#     output = "It's cloudy, a good day to relax indoors."
# elif weather_types == "snowy":
#     output = "It's snowy, bundle up and enjoy the snow!"
# elif weather_types == "rainy":
#     output = "It's rainy, take an umbrella if you go outside."
# else:
#     output = "Unknown weather type. Please enter sunny, cloudy, snowy, or rainy."

# print(output)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

# ADVANCED PROGRAM

weather_types = ["sunny", "cloudy", "snowy", "rainy"]
actions = [
    "It's sunny, go for a walk!",
    "It's cloudy, a good day to relax indoors.",
    "It's snowy, bundle up and enjoy the snow!",
    "It's rainy, take an umbrella if you go outside."
]

# Get weather input from the user
current_weather = input("Enter the current weather (sunny, cloudy, snowy, rainy): ").lower()

# Check if user input is in weather_types list
if current_weather in weather_types:
    # Get the corresponding action from the actions list
    index = weather_types.index(current_weather)
    print(actions[index])
else:
    print("Unknown weather type. Please enter sunny, cloudy, snowy, or rainy.")
