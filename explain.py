# line one explains the name of the data file is being used
# line two defines the function and is given the name load_data
# line three starts a try and except block to handle the potential errors while handling the loading of the data file
#  line four uses an open file function to open the data file in read mode
#  line five makes use of a variable function called lines to store the lines of the data file into a list. (lines can be seen as a list containig every line from the file)
# line six closes the file after reading it
# line seven uses a variable called name to store the first line of the data file after stripping any whitespace
# line eight uses a variable called balance Get the second line, remove the newline, convert it from text into a decimal number, and store it in the variable balance
# line nine makes a list called expenses to store the expenses data
# line ten makes use of a loop for line in lines[2:](starting from the 3rd position to the end thats what the ':' means) to iterate through the remaining lines of the data file, starting from the third line
#  line eleven splits each line into three parts using the '|' character and assigns them to the variables description, category, and amount
# line twelve appends a dictionary to expenses list with the keys "description", "category", and "amount" and their corresponding values from the line
# line  thirteen to fifteen return the name, balance, and expenses list as a tuple(a collection of values that are stored together, similar to a list)
# line seventeen handles the case where the data file is not found and returns None for name, 0 for balance, and an empty list for expenses
# line nineteen handles any other exceptions that may occur during the loading of the data file, prints
# the error message, and returns None for name, 0 for balance, and an empty list for expenses
