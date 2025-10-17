import json



def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file)
            # print(test)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" *90)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("*" *90)

def add_video(videos):
    name = input("Add video name: ")
    time = input("Add video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print(f"Video '{videos[-1]['name']}' added successfully!") #here is the error

def update_video(videos):
    # list_all_videos(videos)
    # index = int(input("Enter the index to update video: "))
    # if 1 <= index <= len(videos):
    #     name = input("Add video name: ")
    #     time = input("Add video time: ")
    #     videos[index -1] = {"name": name, "time": time}
    #     save_data_helper(videos)
    #     print(f"Video '{videos[index - 1]['name']}' updated successfully!") #here is the error
    # else:
    #     print("Invalid index selected")
     list_all_videos(videos)
     index = int(input("Enter the index to update video: "))
     if 1 <= index <= len(videos):
        old_name = videos[index - 1]['name']  # Get the old video name
        name = input("Add new video name: ")
        time = input("Add new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print(f"Video '{old_name}' successfully updated to '{name}'!")  # Updated message
     else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index to delete video: "))
    if 1 <= index <= len(videos):
        deleted_video_name = videos[index - 1]['name']  # Store the name before deletion
        del videos[index - 1]
        save_data_helper(videos)
        print(f"Video '{deleted_video_name}' deleted successfully!")  # Corrected message
    else:
        print("Invalid index selected")


def main():
    videos = load_data()

    while True:
        print("\nPlease select an option")
        print("1. To List the videos")
        print("2. Add the video")
        print("3. Update the video")
        print("4. Delete the video")
        print("5. Exit the app")
        choice = input("Enter options: ")
        # print(videos)
    
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
                break
                

if __name__ ==  "__main__":
    main() 