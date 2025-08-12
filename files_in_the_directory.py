#this python script is used to generate a list of all the files in the current directory
import os
def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        return files
    except Exception as e: # Handle any exceptions that occur
        print(f"An error occurred: {e}")
        return []
    
if __name__ == "__main__":
    current_directory = os.getcwd() # Get the current working directory
    print(f"Current Directory: {current_directory}")
    files = list_files_in_directory(current_directory) # List files in the current directory
    for file in files:
        print(file)
    print("Files in the current directory:")