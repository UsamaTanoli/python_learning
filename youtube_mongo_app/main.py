from pymongo import MongoClient
from bson import ObjectId
from urllib.parse import quote_plus

# URL encode the password
username = "ytmanager"
password = quote_plus("Experiaz3@@123")  # Escapes the special characters in the password
uri = f"mongodb+srv://{username}:{password}@cluster0.6z4wc.mongodb.net/,tlsAllowedInvalidCertificate=True"

client = MongoClient(uri)
db = client['ytmanager']
video_collection = db['videos']

# print(video_collection)
# print(type(video_collection))

def list_videos():
    print("\n")
    print("*"*80)
    for video in video_collection.find():
        # print(video)
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}.")
    print("*"*80)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
        video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})
    

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\nPlease select an option.....")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video id to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter video id to be delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid input!")





if __name__ == "__main__":
    main()