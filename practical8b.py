# Program to copy python file without comments

# Take file names from user
source = input("Enter source python file name: ")
destination = input("Enter destination file name: ")

# Open files
src_file = open(source, "r")
dest_file = open(destination, "w")

print("\nContent of Source File:\n")

for line in src_file:
    print(line, end="")          # Print source file content
    
    # Skip comments
    stripped = line.strip()
    if not stripped.startswith("#"):
        dest_file.write(line)

src_file.close()
dest_file.close()

print("\n\nContent copied to destination file (without comments).\n")

# Print destination file content
dest_file = open(destination, "r")

print("Content of Destination File:\n")
print(dest_file.read())

dest_file.close()