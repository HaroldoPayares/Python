# define the variable as "10"
types_of_people = 10
# assign to 'x' a string, also that string contains another string: types_of_people
x = f"There are {types_of_people} types_of_people."

# define the variable as "binary"
binary = "binary"
# define the variable as "don't"
do_not = "don't"
# assign to 'y' a string, also that sring contains twoothers strings: binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# print on screen the variable
print(x)
# print on screen the variable
print(y)

# print the x variable inside the string
print(f"I said: {x}")
# print the y variable inside the string
print(f"I also said: '{y}'")

# define hilarious variable with False value
hilarious = False
# define joke_evaluation variable with a string value that contains another string
joke_evaluation = "Isn't that joke so funny?! {}"

# print on screen the hilarious variable
print(joke_evaluation.format(hilarious))

# assign a string to w variable
w = "This is the left side of..."
# asign a string to e variable
e = "a string with a right side."

# print on screen w and e variables
print(w + e)
