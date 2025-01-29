import os
import subprocess
import sys

# Get the virtual environment's Python path
venv_python = os.path.join(os.path.dirname(__file__), "venv", "Scripts", "python.exe")

# Fallback to system Python if venv is missing
python_executable = venv_python if os.path.exists(venv_python) else sys.executable

# Define available bot features and their corresponding script files
FEATURES = {
    "1": ("Auto Add Friends", "auto_add_friends.py"),
    "2": ("Auto Reply to Story Mentions", "auto_reply_story.py"),
    "3": ("Auto Streaks Manager", "auto_streaks.py"),
    "4": ("Auto Message Friends", "auto_message_friends.py"),
    "5": ("Mass Messaging", "mass_messaging.py"),
    "6": ("Schedule Post", "schedule_post.py"),
    "7": ("Auto View Stories", "auto_view_story.py"),
    "8": ("Exit", None)
}

def main():
    while True:
        print("\n===== Snapchat Bot Features =====")
        for key, (name, _) in FEATURES.items():
            print(f"{key}. {name}")
        
        choice = input("\nEnter the number of the feature you want to run: ").strip()

        if choice in FEATURES:
            if FEATURES[choice][1] is None:
                print("Exiting...")
                break

            script_path = os.path.join(os.path.dirname(__file__), 'bot_features', FEATURES[choice][1])
            print(f"\nRunning {FEATURES[choice][0]}...\n")

            # Run the script using the correct Python interpreter
            subprocess.run([python_executable, script_path])
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()