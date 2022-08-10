#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
#another  **kwargs    (add=,num=,count=,)

#important   arg  come before  unlimited args  interpreter this way knows args 
# interpreter care about  order  of parameter
# like  this example ▶ def arg_printer(a, b, *args, option=True, **kwargs):
# We can use both *args and **kwargs in a function but *args must be put before **kwargs.
#https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749
func1()
print(func1())
print(func1)
# function not include parentheses mean i want  definition  of function as object thats passed to thing  like object
print(func2(10, 20))
print(cube(3))
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
print(multi_add(4, 5, 10, 4))
