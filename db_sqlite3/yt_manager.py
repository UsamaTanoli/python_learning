# import sqlite3

# # Establish connection
# con = sqlite3.connect('yt_videos.db')
# cur = con.cursor()

# # Create the video table if it doesn't exist
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS video (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         time TEXT NOT NULL
#     )
# """)

# # Function to list videos
# # def list_video():
# #     cur.execute("SELECT * FROM video")  # Use the correct table name
# #     for row in cur.fetchall():
# #         print(row)


# def list_video():
#     cur.execute("SELECT * FROM video")  # Query to get all videos
#     videos = cur.fetchall()
#     if videos:
#         print("\nVideo ID | Name             | Time")
#         print("---------------------------------------")
#         for video in videos:
#             # Printing each video in a more readable format
#             print(f"{video[0]}       | {video[1]:<15} | {video[2]}")
#     else:
#         print("No videos found.")


# # Function to add a new video
# def add_video(name, time):
#     cur.execute("INSERT INTO video (name, time) VALUES (?, ?)", (name, time))  # Correct INSERT syntax
#     con.commit()

# # Function to update an existing video
# def update_video(video_id, new_name, new_time):
#     cur.execute("UPDATE video SET name=?, time=? WHERE id=?", (new_name, new_time, video_id))  # Fixed typo
#     con.commit()

# # Function to delete a video by ID
# def delete_video(video_id):
#     cur.execute("DELETE FROM video WHERE id=?", (video_id,))  # Added 'FROM' keyword
#     con.commit()

# # Main menu loop
# def main():
#     while True:
#         print("\nPlease select an option...")
#         print("1. List videos")
#         print("2. Add video")
#         print("3. Update video")
#         print("4. Delete video")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             list_video()
#         elif choice == "2":
#             name = input("Enter video name: ")
#             time = input("Enter video time: ")
#             add_video(name, time)
#         elif choice == "3":
#             video_id = int(input("Enter video ID to update: "))
#             new_name = input("Enter new video name: ")
#             new_time = input("Enter new video time: ")
#             update_video(video_id, new_name, new_time)
#         elif choice == "4":
#             video_id = int(input("Enter video ID to delete: "))
#             delete_video(video_id)
#         elif choice == "5":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()









import sqlite3

def create_connection():
    """Create a connection to the SQLite database."""
    try:
        con = sqlite3.connect('yt_videos.db')
        return con
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(con):
    """Create the video table if it doesn't exist."""
    try:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS video (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
        """)
        con.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def reset_sequence(con):
    """Reset the auto-increment sequence when all records are deleted."""
    try:
        cur = con.cursor()
        # Check if the table is empty
        cur.execute("SELECT COUNT(*) FROM video")
        count = cur.fetchone()[0]
        
        if count == 0:
            # Reset the SQLite sequence
            cur.execute("DELETE FROM sqlite_sequence WHERE name='video'")
            con.commit()
            print("Video ID sequence reset.")
    except sqlite3.Error as e:
        print(f"Error resetting sequence: {e}")

def list_video(con):
    """List all videos in the database."""
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM video")
        videos = cur.fetchall()
        
        if not videos:
            print("No videos found.")
        else:
            print("\nVideo List:")
            print("ID | Name | Time")
            print("-" * 30)
            for video in videos:
                print(f"{video[0]} | {video[1]} | {video[2]}")
    except sqlite3.Error as e:
        print(f"Error listing videos: {e}")

def add_video(con, name, time):
    """Add a new video to the database."""
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO video (name, time) VALUES (?, ?)", (name, time))
        con.commit()
        print("Video added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding video: {e}")

def update_video(con, video_id, name, time):
    """Update an existing video in the database."""
    try:
        cur = con.cursor()
        cur.execute("UPDATE video SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
        
        if cur.rowcount > 0:
            con.commit()
            print("Video updated successfully!")
        else:
            print(f"No video found with ID {video_id}")
    except sqlite3.Error as e:
        print(f"Error updating video: {e}")

def delete_video(con, video_id):
    """Delete a video from the database."""
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM video WHERE id = ?", (video_id,))
        
        if cur.rowcount > 0:
            con.commit()
            print("Video deleted successfully!")
            
            # Check if the table is now empty and reset sequence if needed
            cur.execute("SELECT COUNT(*) FROM video")
            count = cur.fetchone()[0]
            if count == 0:
                reset_sequence(con)
        else:
            print(f"No video found with ID {video_id}")
    except sqlite3.Error as e:
        print(f"Error deleting video: {e}")

def main():
    # Create database connection
    con = create_connection()
    
    if con is None:
        return
    
    # Create table if not exists
    create_table(con)
    
    while True:
        print("\n--- YouTube Video Manager ---")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        try:
            if choice == "1":
                list_video(con)
            elif choice == "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(con, name, time)
            elif choice == "3":
                video_id = input("Enter video id to update: ")
                name = input("Enter new video name: ")
                time = input("Enter new video time: ")
                update_video(con, video_id, name, time)
            elif choice == "4":
                video_id = input("Enter video id to delete: ")
                delete_video(con, video_id)
            elif choice == "5":
                break
            else:
                print("Invalid option. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Close the database connection
    con.close()
    print("Thank you for using YouTube Video Manager!")

if __name__ == "__main__":
    main()