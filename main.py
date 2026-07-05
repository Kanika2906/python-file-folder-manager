from pathlib import Path 
import os
import shutil

def create_folder():
    try:
        name = input("Please tell your folder name")
        p = Path(name) #gives path of the name of folder
        p.mkdir() #makes a folder
        print("folder created successfully!")
    except Exception as err:
        print(f"sorry an error occured as {err}")

def read_folder():
    p = Path("") #gives path where u exist
    items = list(p.rglob('*')) #reads all the files where u exist
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")

def update_folder():
    try:
        read_folder()
        old_name = input("Please tell which folder you want to update")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("please tell your new folder name :-")
            new_p = Path(new_name)
            p.rename(new_p)
            print("your folder name is updated successfully ")
        else:
            print("sorry no such folder exists.")
    except Exception as err:
        print(f"An error occured as {err}")

def delete_folder():
    try:
        read_folder()
        name = input("Please tell which folder you want to delete")
        p = Path(name)
        if p.exists() and p.is_dir() and p.resolve():
            shutil.rmtree(p) #deletes folder if it contains file inside it also 
            #p.rmdir() #works only if the folder or directory is empty so we use shutil
            print("Folder deleted successfully!")
        else:
            print("no such folder exists")
    except Exception as err:
        print(f"There is an error as {err}")

def create_file():
    try:
        read_folder()
        name = input("Please tell your file name")
        p = Path(name)
        if not p.exists():
            with open(name,"w") as fs:
                data = input("Write what you want in this file")
                fs.write(data)
                print("file created successfully!")
        else:
            print("this name file already exists!")
    except Exception as err:
        print(f"An error occured as {err}")

def read_file():
    try:
        read_folder()
        name = input("please tell your file name:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name,"r") as fs:
                print("Your file content is :-")
                print(fs.read())
        else:
            print("sorry no such file exists.")
    except Exception as err:
        print(f"There is an error as {err}")

def update_file():
    try:
        read_folder()
        name = input("please tell your file name:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Options:-")
            print("1. Renaming the file")
            print("2. Appending something in the file")
            print("3. For overwriting the file")
            choice = int(input("tell your choice"))

            if choice == 1:
                new_name = input("Tell your new name with extension")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("Your file name is changed successfully!")
                else:
                    print("sorry this file already exists!")

            elif choice == 2:
                with open(name,"a") as f:
                    content = input("enter the content to append")
                    f.write(" "+content)
                print("Data appended successfully ")
            
            elif choice == 3:
                with open(name,"w")as fs:
                    content = input("enter the content to append")
                    fs.write(content)
                print("Data written successfully ")
    except Exception as err:
        print(f"An error occured as {err}")


def delete_file():
    try:
        read_folder()
        name = input("Enter the file you want to delete")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("Deleted successfully !")
        else:
            print("sorry no such file exists!")

    except Exception as err:
        print("An error occured as {err}")

if __name__ == "__main__":
    while True:
        print(Path.cwd())
        print("Options : --")

        print("1. Create a folder")
        print("2. Read files and folders")
        print("3. Update the folder")
        print("4. Delete the folder")
        print("5. Create a file")
        print("6. Read a file")
        print("7. Update a file")
        print("8. Delete a file")
        print("9. Exit")

        choice = int(input("Please choose your options"))

        if choice == 1:
            create_folder()

        elif choice == 2:
            read_folder()

        elif choice == 3:
            update_folder()

        elif choice == 4:
            delete_folder()

        elif choice == 5:
            create_file()

        elif choice == 6:
            read_file()

        elif choice == 7:
            update_file()

        elif choice == 8:
            delete_file()

        elif choice == 9:
            exit()
        
        else:
            print("Invalid choice")
