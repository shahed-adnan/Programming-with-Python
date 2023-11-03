# define a function
def add_Three(input_var):
    output_var = input_var + 3
    return output_var


# function with multiple arguments
def total_marks(english, math, physics):
    return english + math + physics


new_number = add_Three(10)
print(new_number)
print(total_marks(85, 100, 95))
