import os

def rename_files_in_folder(folder_path):
    """
    Renames all files in the specified folder by prepending "draft_" to their names.

    Args:
        folder_path (str): The path to the folder containing the files to rename.
    """
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return  # Exit the function if the folder doesn't exist

    # Get a list of all files in the folder
    try:
        files = os.listdir(folder_path)
    except OSError as e:
        print(f"Error reading folder contents: {e}")
        return

    # Iterate through the files and rename them
    for filename in files:
        # Construct the full file path
        old_filepath = os.path.join(folder_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(old_filepath):
            # Construct the new file name
            new_filename = "draft_" + filename
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            try:
                os.rename(old_filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")
        else:
            print(f"Skipping '{filename}' (not a file)")

if __name__ == "__main__":
    # Get the folder path from the user
    folder_path = input("Enter the path to the folder: ")
    # Remove any leading/trailing quotes
    folder_path = folder_path.strip('"').strip("'")

    # Call the function to rename the files
    rename_files_in_folder(folder_path)

    print("File renaming process completed.")
