




# from pymongo import MongoClient
# from bson import ObjectId
# from urllib.parse import quote_plus

# # URL encode the password
# username = "ytmanager"
# password = quote_plus("Experiaz3@@123")  # Escapes the special characters in the password
# uri = f"mongodb+srv://{username}:{password}@cluster0.6z4wc.mongodb.net/,tlsAllowedInvalidCertificate=True"

# client = MongoClient(uri)
# db = client['ytmanager']
# video_collection = db['videos']
# counter_collection = db['counters']


# def get_next_id():
#     """Increments and returns the next available video ID."""
#     result = counter_collection.find_one_and_update(
#         {"_id": "video_id"}, 
#         {"$inc": {"seq": 1}}, 
#         return_document=True, 
#         upsert=True
#     )
#     return result['seq']


# def list_videos():
#     """List all videos, falling back to _id if video_id is missing."""
#     print("\n")
#     print("*" * 80)
#     for video in video_collection.find():
#         video_id = video.get('video_id', video['_id'])  # Use 'video_id' if available, otherwise fallback to '_id'
#         print(f"ID: {video_id}, Name: {video['name']}, Time: {video['time']}.")
#     print("*" * 80)


# def add_video(name, time):
#     """Add a new video with an auto-incremented ID."""
#     new_id = get_next_id()  # Get the next numeric ID
#     video_collection.insert_one({"video_id": new_id, "name": name, "time": time})
#     print(f"Added video with ID: {new_id}")


# def update_video(video_id, new_name, new_time):
#     """Update a video if the video_id is valid."""
#     try:
#         result = video_collection.update_one(
#             {"video_id": int(video_id)},  # Use numeric ID
#             {"$set": {"name": new_name, "time": new_time}}
#         )

#         if result.matched_count == 0:
#             print("No video found with the provided ID.")
#         elif result.modified_count == 0:
#             print("No changes were made to the video.")
#         else:
#             print("Video updated successfully.")
    
#     except Exception as e:
#         print(f"An error occurred: {e}")


# def delete_video(video_id):
#     """Delete a video if the video_id is valid."""
#     try:
#         result = video_collection.delete_one({"video_id": int(video_id)})

#         if result.deleted_count == 0:
#             print("No video found with the provided ID.")
#         else:
#             print("Video deleted successfully.")
    
#     except Exception as e:
#         print(f"An error occurred: {e}")


# def add_video_ids_to_existing_documents():
#     """Add auto-incrementing video_id to all documents that don't have it."""
#     last_id = counter_collection.find_one({"_id": "video_id"})  # Get the current highest ID
#     last_id = last_id['seq'] if last_id else 0

#     # Find all documents without a 'video_id'
#     videos_without_id = video_collection.find({"video_id": {"$exists": False}})
    
#     count = 0
#     for video in videos_without_id:
#         last_id += 1
#         video_collection.update_one(
#             {"_id": video['_id']}, 
#             {"$set": {"video_id": last_id}}
#         )
#         count += 1

#     print(f"Updated {count} documents with new video IDs.")


# def main():
#     # Ensure all old videos have video_id before continuing
#     add_video_ids_to_existing_documents()

#     while True:
#         print("\nPlease select an option.....")
#         print("1. List videos")
#         print("2. Add video")
#         print("3. Update video")
#         print("4. Delete video")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             list_videos()
        
#         elif choice == "2":
#             name = input("Enter video name: ")
#             time = input("Enter video time: ")
#             add_video(name, time)
        
#         elif choice == "3":
#             video_id = input("Enter video ID to update: ")

#             # Ensure the ID is numeric
#             if not video_id.isdigit():
#                 print("Invalid video ID format. Please enter a numeric ID.")
#                 continue  # Go back to the main menu

#             # Proceed if the ID is valid
#             name = input("Enter new video name: ")
#             time = input("Enter new video time: ")
#             update_video(video_id, name, time)
        
#         elif choice == "4":
#             video_id = input("Enter video ID to delete: ")

#             # Ensure the ID is numeric
#             if not video_id.isdigit():
#                 print("Invalid video ID format. Please enter a numeric ID.")
#                 continue  # Go back to the main menu

#             # Proceed if the ID is valid
#             delete_video(video_id)
        
#         elif choice == "5":
#             break
        
#         else:
#             print("Invalid input!")


# if __name__ == "__main__":
#     main()























import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
from urllib.parse import quote_plus

# Load environment variables from .env file
load_dotenv()

class VideoManager:
    def __init__(self):
        """Initialize the MongoDB connection."""
        # Retrieve credentials from environment variables
        username = os.getenv('MONGO_USERNAME')
        password = os.getenv('MONGO_PASSWORD')
        
        if not username or not password:
            raise ValueError("MongoDB username and password must be set in environment variables")
        
        try:
            # Improved URI construction
            uri = (
                f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}"
                "@cluster0.6z4wc.mongodb.net/ytmanager?retryWrites=true&w=majority"
            )
            
            # Create a MongoDB client with more robust connection options
            self.client = MongoClient(uri, 
                serverSelectionTimeoutMS=5000,  # 5 second timeout
                connectTimeoutMS=5000
            )
            
            # Verify the connection
            self.client.admin.command('ismaster')
            
            self.db = self.client['ytmanager']
            self.video_collection = self.db['videos']
            self.counter_collection = self.db['counters']
        
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    def __del__(self):
        """Ensure connection is closed when object is deleted."""
        if hasattr(self, 'client'):
            self.client.close()

    def validate_input(self, name, time):
        """Validate video input."""
        if not name or not name.strip():
            raise ValueError("Video name cannot be empty")
        if not time or not time.strip():
            raise ValueError("Video time cannot be empty")
        return name.strip(), time.strip()

    def get_next_id(self):
        """Increments and returns the next available video ID."""
        try:
            result = self.counter_collection.find_one_and_update(
                {"_id": "video_id"}, 
                {"$inc": {"seq": 1}}, 
                return_document=True, 
                upsert=True
            )
            return result['seq']
        except PyMongoError as e:
            print(f"Error getting next ID: {e}")
            return None

    def list_videos(self):
        """List all videos with improved formatting."""
        try:
            videos = list(self.video_collection.find())
            
            if not videos:
                print("No videos found.")
                return
            
            print("\n" + "=" * 50)
            print("VIDEO CATALOG")
            print("=" * 50)
            
            for video in videos:
                video_id = video.get('video_id', video['_id'])
                print(f"ID: {video_id}")
                print(f"Name: {video['name']}")
                print(f"Time: {video['time']}")
                print("-" * 50)
        
        except PyMongoError as e:
            print(f"Error listing videos: {e}")

    def add_video(self, name, time):
        """Add a new video with input validation."""
        try:
            # Validate inputs
            name, time = self.validate_input(name, time)
            
            # Get next ID
            new_id = self.get_next_id()
            if new_id is None:
                return
            
            # Insert video
            result = self.video_collection.insert_one({
                "video_id": new_id, 
                "name": name, 
                "time": time
            })
            
            print(f"Added video with ID: {new_id}")
            return new_id
        
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except PyMongoError as e:
            print(f"Database Error: {e}")

    def update_video(self, video_id, new_name, new_time):
        """Update a video with comprehensive error handling."""
        try:
            # Validate inputs
            new_name, new_time = self.validate_input(new_name, new_time)
            
            # Convert video_id to integer
            video_id = int(video_id)
            
            # Update operation
            result = self.video_collection.update_one(
                {"video_id": video_id},
                {"$set": {"name": new_name, "time": new_time}}
            )

            if result.matched_count == 0:
                print(f"No video found with ID: {video_id}")
            elif result.modified_count > 0:
                print(f"Video with ID {video_id} updated successfully.")
        
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except PyMongoError as e:
            print(f"Database Error: {e}")

    def delete_video(self, video_id):
        """Delete a video with comprehensive error handling."""
        try:
            # Convert video_id to integer
            video_id = int(video_id)
            
            # Delete operation
            result = self.video_collection.delete_one({"video_id": video_id})

            if result.deleted_count == 0:
                print(f"No video found with ID: {video_id}")
            else:
                print(f"Video with ID {video_id} deleted successfully.")
        
        except ValueError:
            print("Invalid video ID. Please enter a numeric ID.")
        except PyMongoError as e:
            print(f"Database Error: {e}")

def main():
    try:
        # Create video manager instance
        video_manager = VideoManager()

        while True:
            print("\n--- YouTube Video Manager ---")
            print("1. List videos")
            print("2. Add video")
            print("3. Update video")
            print("4. Delete video")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                video_manager.list_videos()
            
            elif choice == "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                video_manager.add_video(name, time)
            
            elif choice == "3":
                video_id = input("Enter video ID to update: ")
                name = input("Enter new video name: ")
                time = input("Enter new video time: ")
                video_manager.update_video(video_id, name, time)
            
            elif choice == "4":
                video_id = input("Enter video ID to delete: ")
                video_manager.delete_video(video_id)
            
            elif choice == "5":
                break
            
            else:
                print("Invalid option. Please try again.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()