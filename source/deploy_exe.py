"""


"""
import os
import subprocess

import PyInstaller

def create_exe(script_path):
    """
    Create an executable from a Python script using PyInstaller.

    :param script_path: The path to the Python script.
    :return: True if the executable was created successfully, False otherwise.
    """
    # Check if PyInstaller is installed
    try:
        import pyinstaller
    except ImportError:
        # Install PyInstaller
        print("PyInstaller is not installed. Installing now...")
        try:
            subprocess.run(['pip', 'install', 'pyinstaller'])
        except Exception as e:
            print(f"Error installing PyInstaller: {e}")
            return False

    # Check if the script file exists
    if not os.path.isfile(script_path):
        print(f"Error: '{script_path}' is not a file.")
        return False

    # Run PyInstaller to create the executable
    try:
        subprocess.run(['pyinstaller', script_path])
        return True
    except Exception as e:
        print(f"Error creating executable: {e}")
        return False


if __name__ == "__main__":
    create_exe('qtube.py')
