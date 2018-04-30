# import the method "argv" from "sys" library
from sys import argv

# pass the script and text file arguments to the "arguments vector"
script, input_file = argv

# designated function to read the file
def print_all(f):
    print(f.read())

# designated function to take the file pointer to the first line
def rewind(f):
    f.seek(0)

# defined function to print out a line from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open the file and set it to the "current_file" namespace
current_file = open(input_file)

print("first let's print the whole file:\n")

# call the "print_all" function to print the file content on screen
print_all(current_file)

print ("Now let's rewind, kind of like tape.")

# call the "rewind" function to take the file pointer to the first line
rewind(current_file)

print("Let's print three lines:" )

# set "current_line" to 1 then pass the arguments to the "print_line" function to print on screen the current line
current_line = 1
print_a_line(current_line, current_file)

# add 1 to the current line position then pass the arguments to the "print_line" function to print on screen the current line
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
