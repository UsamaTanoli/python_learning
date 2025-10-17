# import json
# import os
# import sys
# import time
# import platform
# from pathlib import Path
# from rich.console import Console
# from rich.table import Table
# from rich.panel import Panel
# from rich.text import Text
# from rich.progress import Progress, SpinnerColumn, TextColumn
# from rich.syntax import Syntax

# # Try to import readline for better input handling
# try:
#     import readline
# except ImportError:
#     pass

# class InputHandler:
#     """Handle user inputs with improved functionality."""
#     @staticmethod
#     def get_input(prompt, validator=None, default=None):
#         """
#         Get user input with optional validation and default value.
        
#         Args:
#             prompt (str): Input prompt message
#             validator (callable, optional): Function to validate input
#             default (str, optional): Default value if input is empty
        
#         Returns:
#             str: Validated input
#         """
#         while True:
#             try:
#                 # Use input with readline support for better editing
#                 if default:
#                     prompt_text = f"{prompt} [{default}]: "
#                 else:
#                     prompt_text = f"{prompt}: "
                
#                 user_input = input(prompt_text).strip()
                
#                 # Use default if input is empty
#                 if not user_input and default:
#                     return default
                
#                 # Validate input if validator is provided
#                 if validator:
#                     if validator(user_input):
#                         return user_input
#                     print("Invalid input. Please try again.")
#                 else:
#                     return user_input
            
#             except KeyboardInterrupt:
#                 print("\nInput cancelled.")
#                 return None
#             except Exception as e:
#                 print(f"An error occurred: {e}")

# class ConfigManager:
#     """Manage application configuration."""
#     def __init__(self, config_path='config.json'):
#         self.config_path = Path(config_path)
#         self.default_config = {
#             'filename': 'youtube.txt',
#             'banner_message': 'YouTube Video Manager',
#             'duration_format': 'MM:SS',
#             'help_file': 'help.txt'
#         }
#         self.config = self.load_config()

#     def load_config(self):
#         """Load configuration from file or create default."""
#         try:
#             if self.config_path.exists():
#                 with open(self.config_path, 'r') as f:
#                     return json.load(f)
#             else:
#                 self.save_config(self.default_config)
#                 return self.default_config
#         except Exception as e:
#             print(f"Error loading config: {e}")
#             return self.default_config

#     def save_config(self, config):
#         """Save configuration to file."""
#         try:
#             with open(self.config_path, 'w') as f:
#                 json.dump(config, f, indent=4)
#         except Exception as e:
#             print(f"Error saving config: {e}")

#     def get(self, key):
#         """Get a configuration value."""
#         return self.config.get(key, self.default_config.get(key))

# class YouTubeManager:
#     def __init__(self, config_manager):
#         self.config = config_manager
#         self.filename = self.config.get('filename')
#         self.console = Console()
#         self.videos = self.load_data()
#         self.input_handler = InputHandler()

#     def load_data(self):
#         """
#         Load video data from the configured filename.
#         Creates the file if it doesn't exist.
        
#         Returns:
#             list: List of video dictionaries
#         """
#         try:
#             # Ensure the file exists
#             if not os.path.exists(self.filename):
#                 with open(self.filename, 'w') as f:
#                     json.dump([], f)
            
#             # Read the data
#             with open(self.filename, 'r') as f:
#                 # Handle empty file scenario
#                 file_contents = f.read().strip()
#                 if not file_contents:
#                     return []
                
#                 # Reset file pointer to beginning
#                 f.seek(0)
#                 return json.load(f)
        
#         except json.JSONDecodeError:
#             # If file is not valid JSON, return empty list
#             print(f"Warning: {self.filename} contains invalid JSON. Starting with an empty list.")
#             return []
#         except Exception as e:
#             print(f"Error loading data from {self.filename}: {e}")
#             return []

#     def save_data(self):
#         """
#         Save video data to the configured filename.
#         """
#         try:
#             with open(self.filename, 'w') as f:
#                 json.dump(self.videos, f, indent=4)
#         except Exception as e:
#             print(f"Error saving data to {self.filename}: {e}")

#     def cross_platform_clear_screen(self):
#         """Cross-platform screen clearing."""
#         system = platform.system().lower()
#         if system == 'windows':
#             os.system('cls')
#         else:
#             os.system('clear')

#     def display_banner(self):
#         """Display application banner."""
#         banner_message = self.config.get('banner_message')
#         banner = Panel(
#             Text(banner_message, style="bold blue"),
#             border_style="green",
#             expand=False
#         )
#         self.console.print(banner)

#     def loading_animation(self, message, duration=2):
#         """Create a loading animation."""
#         with Progress(
#             SpinnerColumn(),
#             TextColumn("[progress.description]{task.description}"),
#             transient=True
#         ) as progress:
#             progress.add_task(description=message, total=None)
#             time.sleep(duration)

#     def list_all_videos(self):
#         """List all videos in a rich table format."""
#         self.cross_platform_clear_screen()
#         self.display_banner()

#         if not self.videos:
#             self.console.print("[yellow]No videos found![/yellow]")
#             input("Press Enter to continue...")
#             return

#         table = Table(title="YouTube Video List")
#         table.add_column("No.", style="cyan")
#         table.add_column("Name", style="magenta")
#         table.add_column("Duration", style="green")

#         for idx, video in enumerate(self.videos, 1):
#             table.add_row(str(idx), video['name'], video['time'])

#         self.console.print(table)
#         input("Press Enter to continue...")

#     def add_video(self):
#         """Add a new video with validation."""
#         self.cross_platform_clear_screen()
#         self.display_banner()
        
#         # Validate name is not empty
#         def name_validator(value):
#             return bool(value.strip())
        
#         # Validate duration format
#         def duration_validator(value):
#             try:
#                 minutes, seconds = map(int, value.split(':'))
#                 return 0 <= minutes < 60 and 0 <= seconds < 60
#             except (ValueError, TypeError):
#                 return False

#         # Get video name
#         name = self.input_handler.get_input(
#             "Enter Video Name", 
#             validator=name_validator
#         )
        
#         # Get video duration
#         duration_format = self.config.get('duration_format')
#         time_input = self.input_handler.get_input(
#             f"Enter Video Duration ({duration_format})", 
#             validator=duration_validator
#         )

#         # Confirmation 
#         confirm = self.input_handler.get_input(
#             "Confirm adding this video? (y/n)", 
#             validator=lambda x: x.lower() in ['y', 'yes', 'n', 'no']
#         )

#         if confirm.lower() in ['y', 'yes']:
#             self.videos.append({'name': name, 'time': time_input})
#             self.save_data()
#             self.loading_animation("Adding video", 1)
#             self.console.print("Video Added Successfully!")

#     def update_video(self):
#         """Update an existing video."""
#         self.cross_platform_clear_screen()
#         self.display_banner()

#         if not self.videos:
#             self.console.print("[yellow]No videos to update![/yellow]")
#             input("Press Enter to continue...")
#             return

#         self.list_all_videos()

#         # Validate index selection
#         def index_validator(value):
#             try:
#                 index = int(value)
#                 return 1 <= index <= len(self.videos)
#             except ValueError:
#                 return False

#         index_input = self.input_handler.get_input(
#             "Enter the number of the video to update", 
#             validator=index_validator
#         )

#         index = int(index_input) - 1
#         current_video = self.videos[index]

#         # Name update
#         new_name = self.input_handler.get_input(
#             f"Enter new name (current: {current_video['name']})", 
#             default=current_video['name']
#         )

#         # Duration update
#         duration_format = self.config.get('duration_format')
#         new_time = self.input_handler.get_input(
#             f"Enter new duration ({duration_format}) (current: {current_video['time']})", 
#             default=current_video['time'],
#             validator=lambda x: ':' in x and len(x.split(':')) == 2
#         )

#         # Confirmation
#         confirm = self.input_handler.get_input(
#             "Confirm update? (y/n)", 
#             validator=lambda x: x.lower() in ['y', 'yes', 'n', 'no']
#         )

#         if confirm.lower() in ['y', 'yes']:
#             self.videos[index] = {'name': new_name, 'time': new_time}
#             self.save_data()
#             self.loading_animation("Updating video", 1)
#             self.console.print("Video Updated Successfully!")

#     def delete_video(self):
#         """Delete a video from the list."""
#         self.cross_platform_clear_screen()
#         self.display_banner()

#         if not self.videos:
#             self.console.print("[yellow]No videos to delete![/yellow]")
#             input("Press Enter to continue...")
#             return

#         self.list_all_videos()

#         # Validate index selection
#         def index_validator(value):
#             try:
#                 index = int(value)
#                 return 1 <= index <= len(self.videos)
#             except ValueError:
#                 return False

#         index_input = self.input_handler.get_input(
#             "Enter the number of the video to delete", 
#             validator=index_validator
#         )

#         index = int(index_input) - 1
#         video_to_delete = self.videos[index]

#         # Confirmation
#         confirm = self.input_handler.get_input(
#             f"Are you sure you want to delete '{video_to_delete['name']}'? (y/n)", 
#             validator=lambda x: x.lower() in ['y', 'yes', 'n', 'no']
#         )

#         if confirm.lower() in ['y', 'yes']:
#             del self.videos[index]
#             self.save_data()
#             self.loading_animation("Deleting video", 1)
#             self.console.print("Video Deleted Successfully!")

#     def display_help(self):
#         """Display help information."""
#         self.cross_platform_clear_screen()
#         self.display_banner()

#         help_file = self.config.get('help_file')
#         try:
#             with open(help_file, 'r') as f:
#                 help_text = f.read()
#                 self.console.print(help_text)
#         except FileNotFoundError:
#             # Default help text if file doesn't exist
#             help_text = """
#             YouTube Video Manager Help:
#             1. List All Videos: View all saved videos
#             2. Add Video: Add a new video to the list
#             3. Update Video: Modify an existing video's details
#             4. Delete Video: Remove a video from the list
#             5. Help: Display this help information
#             6. Exit: Close the application
#             """
#             self.console.print(help_text)

#         input("Press Enter to continue...")

#     def main_menu(self):
#         """Main application loop with menu."""
#         while True:
#             self.cross_platform_clear_screen()
#             self.display_banner()

#             menu_options = [
#                 "List All Videos",
#                 "Add Video",
#                 "Update Video",
#                 "Delete Video",
#                 "Help",
#                 "Exit"
#             ]

#             for i, option in enumerate(menu_options, 1):
#                 self.console.print(f"{i}. {option}")

#             # Input with validation
#             choice = self.input_handler.get_input(
#                 "Enter Your Choice", 
#                 validator=lambda x: x in ['1', '2', '3', '4', '5', '6']
#             )

#             # Execute chosen action
#             if choice == "1":
#                 self.list_all_videos()
#             elif choice == "2":
#                 self.add_video()
#             elif choice == "3":
#                 self.update_video()
#             elif choice == "4":
#                 self.delete_video()
#             elif choice == "5":
#                 self.display_help()
#             elif choice == "6":
#                 self.loading_animation("Exiting application", 1)
#                 break

# def main():
#     try:
#         # Initialize configuration
#         config_manager = ConfigManager()
        
#         # Create help file if not exists
#         help_file = config_manager.get('help_file')
#         if not os.path.exists(help_file):
#             with open(help_file, 'w') as f:
#                 f.write("""
# YouTube Video Manager Help:
# 1. List All Videos: View all saved videos
# 2. Add Video: Add a new video to the list
# 3. Update Video: Modify an existing video's details
# 4. Delete Video: Remove a video from the list
# 5. Help: Display this help information
# 6. Exit: Close the application
# """)
        
#         # Create manager and start the application
#         manager = YouTubeManager(config_manager)
#         manager.main_menu()
#     except KeyboardInterrupt:
#         print("\nApplication terminated by user.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()















import json
import os
import sys
import time
import platform
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
import logging

# Try to import readline for better input handling
try:
    import readline
except ImportError:
    pass

# Set up logging
logging.basicConfig(filename='youtube_manager.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InputHandler:
    """Handle user inputs with improved functionality."""
    @staticmethod
    def get_input(prompt, validator=None, default=None):
        """
        Get user input with optional validation and default value.
        
        Args:
            prompt (str): Input prompt message
            validator (callable, optional): Function to validate input
            default (str, optional): Default value if input is empty
        
        Returns:
            str: Validated input
        """
        while True:
            try:
                if default:
                    prompt_text = f"{prompt} [{default}]: "
                else:
                    prompt_text = f"{prompt}: "
                
                user_input = input(prompt_text).strip()
                
                # Use default if input is empty
                if not user_input and default:
                    return default
                
                # Validate input if validator is provided
                if validator:
                    if validator(user_input):
                        return user_input
                    print("Invalid input. Please try again.")
                else:
                    return user_input
            
            except KeyboardInterrupt:
                print("\nInput cancelled.")
                return None
            except Exception as e:
                print(f"An error occurred: {e}")

class ConfigManager:
    """Manage application configuration."""
    def __init__(self, config_path='config.json'):
        self.config_path = Path(config_path)
        self.default_config = {
            'filename': 'youtube.txt',
            'banner_message': 'YouTube Video Manager',
            'duration_format': 'MM:SS',
            'help_file': 'help.txt'
        }
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from file or create default."""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            else:
                self.save_config(self.default_config)
                return self.default_config
        except Exception as e:
            print(f"Error loading config: {e}")
            return self.default_config

    def save_config(self, config):
        """Save configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")

    def get(self, key):
        """Get a configuration value."""
        return self.config.get(key, self.default_config.get(key))

class YouTubeManager:
    def __init__(self, config_manager):
        self.config = config_manager
        self.filename = self.config.get('filename')
        self.console = Console()
        self.videos = self.load_data()
        self.input_handler = InputHandler()

    def load_data(self):
        """
        Load video data from the configured filename.
        Creates the file if it doesn't exist.
        
        Returns:
            list: List of video dictionaries
        """
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as f:
                    json.dump([], f)
            
            with open(self.filename, 'r') as f:
                file_contents = f.read().strip()
                if not file_contents:
                    return []
                return json.loads(file_contents)
        
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in {self.filename}.")
            self.console.print(f"[red]Error: The file {self.filename} contains invalid JSON.[/red]")
            self.console.print("[yellow]You can either reset the file or fix it manually.[/yellow]")
            action = self.input_handler.get_input(
                "Would you like to reset the file? (y/n)", 
                validator=lambda x: x.lower() in ['y', 'n']
            )
            if action.lower() == 'y':
                self.save_data([])  # Reset the file
                return []
            else:
                sys.exit("Please fix the file manually and restart the program.")
        except Exception as e:
            logging.error(f"Error loading data from {self.filename}: {e}")
            return []

    def save_data(self, videos=None):
        """
        Save video data to the configured filename.
        """
        if videos is not None:
            self.videos = videos
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.videos, f, indent=4)
            logging.info(f"Data saved to {self.filename}.")
        except Exception as e:
            logging.error(f"Error saving data to {self.filename}: {e}")

    def cross_platform_clear_screen(self):
        """Cross-platform screen clearing."""
        system = platform.system().lower()
        if system == 'windows':
            os.system('cls')
        else:
            os.system('clear')

    def display_banner(self):
        """Display application banner."""
        banner_message = self.config.get('banner_message')
        banner = Panel(
            Text(banner_message, style="bold blue"),
            border_style="green",
            expand=False
        )
        self.console.print(banner)

    def loading_animation(self, message, duration=2):
        """Create a loading animation."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        ) as progress:
            progress.add_task(description=message, total=None)
            time.sleep(duration)

    def list_all_videos(self):
        """List all videos in a rich table format."""
        self.cross_platform_clear_screen()
        self.display_banner()

        if not self.videos:
            self.console.print("[yellow]No videos found![/yellow]")
            input("Press Enter to continue...")
            return

        table = Table(title="YouTube Video List")
        table.add_column("No.", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Duration", style="green")

        for idx, video in enumerate(self.videos, 1):
            table.add_row(str(idx), video['name'], video['time'])

        self.console.print(table)
        input("Press Enter to continue...")

    def add_video(self):
        """Add a new video with validation."""
        self.cross_platform_clear_screen()
        self.display_banner()
        
        def name_validator(value):
            return bool(value.strip())
        
        def duration_validator(value):
            try:
                parts = value.split(':')
                if len(parts) == 2:
                    minutes, seconds = map(int, parts)
                    return 0 <= minutes < 60 and 0 <= seconds < 60
                elif len(parts) == 3:
                    hours, minutes, seconds = map(int, parts)
                    return 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60
                return False
            except ValueError:
                return False

        name = self.input_handler.get_input("Enter Video Name", validator=name_validator)
        time_input = self.input_handler.get_input(
            "Enter Video Duration (MM:SS or HH:MM:SS)", 
            validator=duration_validator
        )

        if self.confirm_action("add this video"):
            self.videos.append({'name': name, 'time': time_input})
            self.save_data()
            self.loading_animation("Adding video", 1)
            self.console.print("Video Added Successfully!")

    def update_video(self):
        """Update an existing video."""
        self.cross_platform_clear_screen()
        self.display_banner()

        if not self.videos:
            self.console.print("[yellow]No videos to update![/yellow]")
            input("Press Enter to continue...")
            return

        self.list_all_videos()

        def index_validator(value):
            try:
                index = int(value)
                return 1 <= index <= len(self.videos)
            except ValueError:
                return False

        index_input = self.input_handler.get_input(
            "Enter the number of the video to update", 
            validator=index_validator
        )
        index = int(index_input) - 1
        current_video = self.videos[index]

        new_name = self.input_handler.get_input(
            f"Enter new name (current: {current_video['name']})", 
            default=current_video['name']
        )
        new_time = self.input_handler.get_input(
            f"Enter new duration (current: {current_video['time']})", 
            default=current_video['time'],
            validator=lambda x: ':' in x
        )

        if self.confirm_action("update this video"):
            self.videos[index] = {'name': new_name, 'time': new_time}
            self.save_data()
            self.loading_animation("Updating video", 1)
            self.console.print("Video Updated Successfully!")

    def delete_video(self):
        """Delete a video."""
        self.cross_platform_clear_screen()
        self.display_banner()

        if not self.videos:
            self.console.print("[yellow]No videos to delete![/yellow]")
            input("Press Enter to continue...")
            return

        self.list_all_videos()

        def index_validator(value):
            try:
                index = int(value)
                return 1 <= index <= len(self.videos)
            except ValueError:
                return False

        index_input = self.input_handler.get_input(
            "Enter the number of the video to delete", 
            validator=index_validator
        )
        index = int(index_input) - 1
        video_to_delete = self.videos[index]

        if self.confirm_action(f"delete video '{video_to_delete['name']}'"):
            del self.videos[index]
            self.save_data()
            self.loading_animation("Deleting video", 1)
            self.console.print("Video Deleted Successfully!")

    def confirm_action(self, action_description):
        """Confirm user action."""
        confirmation = self.input_handler.get_input(
            f"Are you sure you want to {action_description}? (y/n)", 
            validator=lambda x: x.lower() in ['y', 'n']
        )
        return confirmation.lower() == 'y'

def main():
    config_manager = ConfigManager()
    yt_manager = YouTubeManager(config_manager)

    while True:
        yt_manager.cross_platform_clear_screen()
        yt_manager.display_banner()
        print("1. List All Videos")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit")
        
        choice = yt_manager.input_handler.get_input("Choose an option", validator=lambda x: x.isdigit() and 1 <= int(x) <= 5)

        if choice == "1":
            yt_manager.list_all_videos()
        elif choice == "2":
            yt_manager.add_video()
        elif choice == "3":
            yt_manager.update_video()
        elif choice == "4":
            yt_manager.delete_video()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
