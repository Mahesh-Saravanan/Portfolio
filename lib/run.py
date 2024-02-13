import os

# Define the path to your working repository
working_directory = r"C:\Users\Maheshsaravanan\Desktop\resume-website-template\resume-website-template\lib"

# Define the path for the output file
output_file_path = r"C:\Users\Maheshsaravanan\Desktop\resume-website-template\resume-website-template\lib\output.txt"

# Function to read text from a file
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Function to write text to the output file
def write_text_to_output_file(output_file_path, text):
    try:
        with open(output_file_path, 'a') as file:
            file.write(text)
            file.write("\n\n")  # Add some separation between file contents
            print(f"Text appended to {output_file_path} successfully.")
    except Exception as e:
        print(f"Error writing to file {output_file_path}: {e}")

# Function to traverse directories and write text files
def write_text_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                text = read_text_from_file(file_path)
                if text is not None:
                    write_text_to_output_file(output_file_path, f"<script>\n{text}\n</script>")

# Call the function with the working directory
write_text_files_in_directory(working_directory)
