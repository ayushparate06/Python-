# Program to copy content of a file into another file in uppercase

# Open source file in read mode
source_file = open("input.txt", "r")

# Read content
content = source_file.read()

# Convert content to uppercase
upper_content = content.upper()

# Open destination file in write mode
dest_file = open("output.txt", "w")

# Write uppercase content
dest_file.write(upper_content)

# Close files
source_file.close()
dest_file.close()

print("File copied successfully with uppercase content.")