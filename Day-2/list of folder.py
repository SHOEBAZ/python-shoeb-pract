folders = input("Please provide list of folders naames with spaces in between:" ).split ()  # last mme spilt dalne se hum user ka input list me convert karre user ko na karne pade isliye usko bas space ke saath folder name do bole

print(folders)

import os

for folder in folders:

    try:    
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name, lools like this folder does not exist:" + folder)
        break

    print(" ===== listing files for the folder - " + folder)
    #print(files)

    for  file in files:
        print(file)

# ab agr user ne file name sahi diye tu thikh hai agr galat hai tu error nahi aana chahiye sahi wali file tu ya folder run hona chahiye tu use exceptional handingling

import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()

