# File Handling Project in Python
# Project Title : File Handling Using Python
# Author        : Prithiv Raj S

import os   # for file delete and file existence checking


# Function to create/write data into a file
def write_file(filename, content):
    try:
        with open(filename, 'w') as f:   # 'w' mode overwrites file if exists
            f.write(content)
        print("\nData successfully written to", filename)
    except Exception as e:
        print("Error while writing file:", e)


# Function to read data from a file
def read_file(filename):
    try:
        with open(filename, 'r') as f:   # 'r' mode for reading
            data = f.read()
        print("\nFile Content:\n")
        print(data)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error while reading file:", e)


# Function to append new content to a file
def append_file(filename, content):
    try:
        with open(filename, 'a') as f:   # 'a' mode appends new content
            f.write(content)
        print("\nData successfully appended to", filename)
    except Exception as e:
        print("Error while appending file:", e)


# Function to display file line by line
def display_file_line_by_line(filename):
    try:
        with open(filename, 'r') as f:
            print("\nDisplaying file content line by line:\n")
            for line in f:
                print(line.strip())  # strip() removes newline characters
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error while displaying file:", e)


# Function to delete a file
def delete_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print("\nFile deleted successfully:", filename)
        else:
            print("File does not exist. Cannot delete.")
    except Exception as e:
        print("Error while deleting file:", e)


# Function to check if a file exists
def check_file_exists(filename):
    if os.path.exists(filename):
        print("\nFile exists:", filename)
    else:
        print("\nFile does not exist.")

#menu
def main():
    filename = "sample.txt"

    while True:
        print("\n========= FILE HANDLING MENU =========")
        print("1. Write to File (Create/Overwrite)")
        print("2. Read File")
        print("3. Append to File")
        print("4. Display File Line by Line")
        print("5. Delete File")
        print("6. Check if File Exists")
        print("7. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            content = input("\nEnter text to write into the file:\n")
            write_file(filename, content)

        elif choice == 2:
            read_file(filename)

        elif choice == 3:
            content = input("\nEnter text to append into the file:\n")
            append_file(filename, "\n" + content)

        elif choice == 4:
            display_file_line_by_line(filename)

        elif choice == 5:
            delete_file(filename)

        elif choice == 6:
            check_file_exists(filename)

        elif choice == 7:
            print("\nExiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
