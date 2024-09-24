def create_file():
    try:
        # Open file in write mode and create the file if it doesn't exist
        with open("my_file.txt", 'w') as file:
            # Writing three lines of text with a mix of strings and numbers
            file.write("Hello, this is the first line.\n")
            file.write("This is line number 2.\n")
            file.write("Number of attempts: 3\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

# File Reading and Display
def read_file():
    try:
        # Open file in read mode
        with open("my_file.txt", 'r') as file:
            # Read and display the content
            content = file.read()
            print("File contents after reading:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# File Appending
def append_to_file():
    try:
        # Open file in append mode
        with open("my_file.txt", 'a') as file:
            # Append three additional lines of text
            file.write("Appending new content here.\n")
            file.write("This is another line added to the file.\n")
            file.write("End of file with line 6.\n")
        print("File updated with appended content.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Error Handling
def handle_file_operations():
    try:
        # Perform all file operations
        create_file()
        read_file()
        append_to_file()
        read_file()  # Read file again to show new content
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

# Run the file operations
if __name__ == "__main__":
    handle_file_operations()
