# importing modules
import os
import string

# defining the main function
def find(name):
    os.system('cls')   # clearing terminal

    paths = []   # defining an empty list of paths

    # defining the drive finder function
    def drive_walk():
        drives = []   # defining empty list of drives

        # iterating over every uppercase letter for each drive
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"   # putting letter as drive name
            if os.path.exists(drive):   # checking if the drive exists
                drives.append(drive)   # adding to drives list if the drive exists
        return drives   # returning the drives list

    # defining the file finder function
    def os_walk():
        # iterating over each drive returned by 'drive_walk' function
        for drive_root in drive_walk(): 
            # iterating over all roots, directories, subdirectories and files inside that drive
            for root, dirs, files in os.walk(drive_root):
                # iterating over every directory
                for dir in dirs:
                    path = os.path.join(root, dir)
                    yield path   # yielding path of directory

                # iterating over every file
                for file in files:
                    path = os.path.join(root, file)
                    yield path   # yielding path of file

    # iterating over each path yielded by 'os_walk' function
    for item in os_walk():
        if name.lower() in item.lower():   # checking if the search matches the file or directory path
            paths.append(item)   # adding the path to the paths list if it matches
    
    # checking if paths list is not empty ( atleast one path is found )
    if paths:
        print('\n') 
        # iterating over each path inside the paths list
        for index, path in enumerate(paths, 1):
            print(f"{index:5}. {path}")   # printing the index and path
        print('\n')
    else:
        print('\n> No path found\n')   # printing 'No path found' if the path list is empty ( no paths were found )

# running the main function
if __name__ == '__main__':
    find(input('> '))   # asking for input and running the find ( main ) function
