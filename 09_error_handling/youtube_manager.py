# import json


# def load_data():
#     try:
#         with open("youtube.txt", "r") as file:
#             test = json.load(file)
#             # print(type(test))
#             return test
#     except FileNotFoundError:
#         return []

# def save_data_helper(videos):
#     with open("youtube.txt", "w") as file:
#         json.dump(videos, file)

# def list_all_videos(videos):
#     print("\n")
#     print("*"*90)
#     for index, video in enumerate(videos, start=1):
#         print(f"{index}. {video['name']}: Duration: {video['time']}")
#     print("*"*90)
#     # for vid in videos:
#     #     print(f"{vid},")

# def add_video(videos):
#     name = input("Enter Video Name: ")
#     time = input("Enter Video Time: ")
#     videos.append({'name': name, 'time': time})
#     save_data_helper(videos)

# def update_video(videos):
#     list_all_videos(videos)
#     index = int(input("Enter The Index Number To Update Video: "))
#     if 1 <= index <= len(videos):
#         name = input("Enter The New Video Name: ")
#         time = input("Enter The New Video Time: ")
#         videos[index -1] = {'name': name, 'time': time}
#         save_data_helper(videos)
#     else:
#         print("Invalid Count Selected")

# def delete_video(videos):
#     list_all_videos(videos)
#     index = int(input("Enter The Index Number To Delete Video: "))
#     if 1 <= index <= len(videos):
#         del videos[index -1]
#         save_data_helper(videos)
#     else:
#         print("Invalid Index Selected")


# def main():
#     videos = load_data()

#     while True:
#         print("\n Youtube Manager | Choose An Option \n")
#         print("1. List All Youtube Videos: ")
#         print("2. Add A Youtube Video: ")
#         print("3. Update Youtube Video: ")
#         print("4. Delete The Video: ")
#         print("5. Exit The App: ")
#         choice = input("Enter The Choise: ")
#         # print(videos)

#         match choice:
#             case "1":
#                 list_all_videos(videos)
#             case "2":
#                 add_video(videos)
#             case "3":
#                 update_video(videos)
#             case "4":
#                 delete_video(videos)
#             case "5":
#                 break
#             case _:
#                 print("Invalid Choice")


# if __name__ == "__main__":
#     main()












# import json
# import time
# import sys
# from colorama import Fore, Back, Style, init

# # Initialize colorama for Windows compatibility
# init(autoreset=True)

# # Load videos from the file
# def load_data():
#     try:
#         with open("youtube.txt", "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []

# # Save videos to the file
# def save_data_helper(videos):
#     with open("youtube.txt", "w") as file:
#         json.dump(videos, file)

# # Simulated loading animation with color
# def loading_animation(message, duration=2):
#     sys.stdout.write(Fore.CYAN + message)
#     sys.stdout.flush()
#     for _ in range(duration):
#         for symbol in "|/-\\":
#             sys.stdout.write(Fore.YELLOW + symbol)
#             sys.stdout.flush()
#             time.sleep(0.1)
#             sys.stdout.write("\b")

# # Typewriter-style effect for displaying text with color
# def typewriter_effect(text, color=Fore.GREEN):
#     for char in text:
#         sys.stdout.write(color + char)
#         sys.stdout.flush()
#         time.sleep(0.05)
#     print()

# # List all videos with a loading animation and color
# def list_all_videos(videos):
#     print("\n")
#     loading_animation("Loading videos... ")
#     print("\n" + Fore.MAGENTA + "*" * 90)
#     for index, video in enumerate(videos, start=1):
#         print(Fore.CYAN + f"{index}. {video['name']}: Duration: {video['time']}")
#     print(Fore.MAGENTA + "*" * 90)

# # Add a new video with a typewriter effect and color
# def add_video(videos):
#     typewriter_effect("Adding a new video...\n", Fore.CYAN)
#     name = input(Fore.GREEN + "Enter Video Name: ")
#     time = input(Fore.GREEN + "Enter Video Time: ")
#     videos.append({'name': name, 'time': time})
#     save_data_helper(videos)
#     typewriter_effect(f"Video '{name}' added successfully!", Fore.GREEN)

# # Update an existing video with animations and color
# def update_video(videos):
#     list_all_videos(videos)
#     try:
#         index = int(input(Fore.YELLOW + "Enter The Index Number To Update Video: "))
#         if 1 <= index <= len(videos):
#             typewriter_effect("Updating the video...\n", Fore.CYAN)
#             name = input(Fore.GREEN + "Enter The New Video Name: ")
            
#             # Simple validation for time (numeric)
#             while True:
#                 time = input(Fore.GREEN + "Enter The New Video Time (in minutes): ")
#                 if time.isdigit():
#                     break
#                 else:
#                     print(Fore.RED + "Please enter a valid number for the video duration (in minutes).")

#             videos[index - 1] = {'name': name, 'time': time}
#             save_data_helper(videos)
#             typewriter_effect(f"Video '{name}' updated with a duration of {time} minutes.", Fore.GREEN)
#         else:
#             typewriter_effect("Invalid Index Selected", Fore.RED)
#     except ValueError:
#         typewriter_effect("Please enter a valid number.", Fore.RED)

# # Delete a video with an animation and color
# def delete_video(videos):
#     list_all_videos(videos)
#     try:
#         index = int(input(Fore.YELLOW + "Enter The Index Number To Delete Video: "))
#         if 1 <= index <= len(videos):
#             video_name = videos[index - 1]['name']
#             del videos[index - 1]
#             save_data_helper(videos)
#             typewriter_effect(f"Video '{video_name}' deleted successfully!", Fore.GREEN)
#         else:
#             typewriter_effect("Invalid Index Selected", Fore.RED)
#     except ValueError:
#         typewriter_effect("Please enter a valid number.", Fore.RED)

# # Main function to handle menu options with colored output
# def main():
#     videos = load_data()

#     while True:
#         print(Fore.BLUE + "\nYoutube Manager | Choose An Option\n")
#         print(Fore.YELLOW + "1. List All Youtube Videos")
#         print(Fore.YELLOW + "2. Add A Youtube Video")
#         print(Fore.YELLOW + "3. Update Youtube Video")
#         print(Fore.YELLOW + "4. Delete A Video")
#         print(Fore.YELLOW + "5. Exit The App")
#         choice = input(Fore.CYAN + "Enter The Choice: ")

#         match choice:
#             case "1":
#                 list_all_videos(videos)
#             case "2":
#                 add_video(videos)
#             case "3":
#                 update_video(videos)
#             case "4":
#                 delete_video(videos)
#             case "5":
#                 typewriter_effect("Exiting the app...", Fore.CYAN)
#                 break
#             case _:
#                 typewriter_effect("Invalid Choice", Fore.RED)


# if __name__ == "__main__":
#     main()












import json
import time
import sys
from colorama import Fore, Style, init
import re

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Load videos from the file
def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save videos to the file
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

# Simulated loading animation with color
def loading_animation(message, duration=2):
    sys.stdout.write(Fore.MAGENTA + message)  # Magenta for loading messages
    sys.stdout.flush()
    for _ in range(duration):
        for symbol in "|/-\\":
            sys.stdout.write(Fore.YELLOW + symbol)  # Yellow for animation symbols
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")

# Typewriter-style effect for displaying text with color
def typewriter_effect(text, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# List all videos with a loading animation and color
def list_all_videos(videos):
    print("\n")
    loading_animation("Loading videos... ")
    print("\n" + Fore.CYAN + "*" * 90)  # Cyan for a list divider
    for index, video in enumerate(videos, start=1):
        print(Fore.BLUE + f"{index}. {video['name']}: Duration: {video['time']}")  # Blue for video list
    print(Fore.CYAN + "*" * 90)

# Function to validate time format (HH:MM:SS or numeric)
def is_valid_time_format(time):
    # Matches HH:MM:SS or numeric durations
    return re.match(r'^(\d{1,2}:\d{2}:\d{2}|\d+)$', time) is not None

# Add a new video with a typewriter effect and color
def add_video(videos):
    typewriter_effect("Adding a new video...\n", Fore.MAGENTA)
    name = input(Fore.YELLOW + "Enter Video Name: ")  # Yellow for input prompts
    time = input(Fore.YELLOW + "Enter Video Time (HH:MM:SS or numeric): ")
    
    while not is_valid_time_format(time):
        print(Fore.RED + "Invalid time format. Please enter HH:MM:SS or numeric.")  # Red for error messages
        time = input(Fore.YELLOW + "Enter Video Time (HH:MM:SS or numeric): ")

    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    typewriter_effect(f"Video '{name}' added successfully!", Fore.GREEN)  # Green for success messages

# Update an existing video with animations and color
def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input(Fore.YELLOW + "Enter The Index Number To Update Video: "))  # Yellow for input
        if 1 <= index <= len(videos):
            typewriter_effect("Updating the video...\n", Fore.MAGENTA)
            name = input(Fore.YELLOW + "Enter The New Video Name: ")

            # Validate time format (HH:MM:SS or numeric)
            while True:
                time = input(Fore.YELLOW + "Enter The New Video Time (HH:MM:SS or numeric): ")
                if is_valid_time_format(time):
                    break
                else:
                    print(Fore.RED + "Invalid time format. Please enter HH:MM:SS or numeric.")

            videos[index - 1] = {'name': name, 'time': time}
            save_data_helper(videos)
            typewriter_effect(f"Video '{name}' updated with a duration of {time}.", Fore.GREEN)
        else:
            typewriter_effect("Invalid Index Selected", Fore.RED)
    except ValueError:
        typewriter_effect("Please enter a valid number.", Fore.RED)

# Delete a video with an animation and color
def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input(Fore.YELLOW + "Enter The Index Number To Delete Video: "))  # Yellow for input
        if 1 <= index <= len(videos):
            video_name = videos[index - 1]['name']
            del videos[index - 1]
            save_data_helper(videos)
            typewriter_effect(f"Video '{video_name}' deleted successfully!", Fore.GREEN)
        else:
            typewriter_effect("Invalid Index Selected", Fore.RED)
    except ValueError:
        typewriter_effect("Please enter a valid number.", Fore.RED)

# Main function to handle menu options with colored output
def main():
    videos = load_data()

    while True:
        print(Fore.BLUE + "\nYoutube Manager | Choose An Option\n")  # Blue for menu title
        print(Fore.CYAN + "1. List All Youtube Videos")
        print(Fore.CYAN + "2. Add A Youtube Video")
        print(Fore.CYAN + "3. Update Youtube Video")
        print(Fore.CYAN + "4. Delete A Video")
        print(Fore.CYAN + "5. Exit The App")
        choice = input(Fore.YELLOW + "Enter The Choice: ")  # Yellow for user input

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                typewriter_effect("Exiting the app...", Fore.MAGENTA)
                break
            case _:
                typewriter_effect("Invalid Choice", Fore.RED)  # Red for invalid choice


if __name__ == "__main__":
    main()
