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
from rich.prompt import Prompt
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

                user_input = Prompt.ask(prompt_text).strip()

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

    def display_splash_screen(self):
        """Display an animated splash screen."""
        splash_text = """
        [bold blue]Welcome to YouTube Video Manager[/bold blue]
        [bold green]Loading...[/bold green]
        """
        self.console.print(Panel(Text(splash_text, justify="center"), expand=False))
        self.loading_animation("Initializing", 3)

def main():
    config_manager = ConfigManager()
    yt_manager = YouTubeManager(config_manager)
    yt_manager.display_splash_screen()

    while True:
        yt_manager.cross_platform_clear_screen()
        yt_manager.display_banner()

        menu = Table(title="Main Menu")
        menu.add_column("Option", style="cyan")
        menu.add_column("Description", style="magenta")
        menu.add_row("1", "List All Videos")
        menu.add_row("2", "Add a Video")
        menu.add_row("3", "Update a Video")
        menu.add_row("4", "Delete a Video")
        menu.add_row("5", "Exit")

        yt_manager.console.print(menu)

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
