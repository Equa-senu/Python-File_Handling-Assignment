# file_handling_assignment.py

# Step 1: File Creation and Writing
try:
    # Create and open the file in write mode
    with open("my_file.txt", 'w') as file:
        # Writing three lines of text, including a mix of strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("This file was created using Python.\n")
        file.write("The number 42 is often referenced as the answer to life.\n")
    print("File created and initial content written successfully.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Step 2: File Reading and Display
try:
    # Open the file in read mode and display its contents
    with open("my_file.txt", 'r') as file:
        print("\nContents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Step 3: File Appending
try:
    # Open the file in append mode and write three additional lines
    with open("my_file.txt", 'a') as file:
        file.write("Appending new content to the file.\n")
        file.write("Python makes file handling simple and powerful.\n")
        file.write("Here is a random number: 12345.\n")
    print("Additional content appended successfully.")
except PermissionError:
    print("Error: You do not have permission to modify this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Step 4: Displaying the updated file contents
try:
    # Open the file again in read mode to show the updated content
    with open("my_file.txt", 'r') as file:
        print("\nUpdated contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling demonstration complete.")
