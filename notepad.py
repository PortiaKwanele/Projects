import os

def create_file():
    """Create a new file and write text to it."""
    filename = input("Enter the name of the file: ")
    text = input("Enter the text you want to write to the file: ")

    with open(filename, 'w') as file:
        file.write(text)

    print("File created and text written successfully.")

def read_file():
    """Read the contents of an existing file."""
    filename = input("Enter the name of the file: ")

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    else:
        print("File not found.")

def update_file():
    """Append text to an existing file."""
    filename = input("Enter the name of the file: ")

    if os.path.exists(filename):
        text = input("Enter the text you want to add to the file: ")

        with open(filename, 'a') as file:
            file.write(text)

        print("Text added to file successfully.")
    else:
        print("File not found.")

while True:
    print("\nNotebook Menu:")
    print("1. Create a new file")
    print("2. Read an existing file")
    print("3. Update an existing file")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        create_file()
    elif choice == '2':
        read_file()
    elif choice == '3':
        update_file()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
