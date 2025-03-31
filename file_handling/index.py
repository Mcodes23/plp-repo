def modify_content(content):
    """Modify the content (example: convert to uppercase)."""
    return content.upper() 

def read_and_write_file():
    """Reads a file, modifies its content, and writes to a new file."""
    try:
        filename = input("Enter the filename to read: ")

        with open(filename, "r") as file:
            content = file.read()

        modified_content = modify_content(content)

        new_filename = f"modified_{filename}"
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()
