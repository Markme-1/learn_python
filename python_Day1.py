"""Basics of python"""

#python Indentation

"""
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

"""
x= 5
if (x < 10):
    print("x is less than 10")
else:
    print("x is grater than 10")


#python comments

"""
in python # is used to create a comments.
in python three inverted commas used to crate a multiple line comments
comments usually used to explain python code.
comments used to make the code more readable

"""
#this is an single line comment
"""
this is 
an multiple line
comment
"""

#python variables

"""
in any programming language variable is used to store data in it.
python has no command to declare a variable 

"""
x =2
y= "python"
z= """this is a 
multiple line string"""#using """ """ triple quots it is possible to write multiple line string
print(x)
print(y)
print(z)
print("\n") #\n is used to create a new line.
      
"""Variables do not need to be declared with any particular type,
 and can even change type after they have been set."""

x= 2 
x= "this is a string"
print(x)

"""If you want to specify the data type of a variable, this can be done with casting."""
x= int(3) #x will be an integer it's 3 here
y= str(5) #here y will be '5' a string
z= float(7) #here z will be 7.0 a float value

"""to see the data type of a variable we can use type() function"""
ver1= 5
ver2= "hello world"
ver3= 8.5

print(type(ver1))
print(type(ver2))
print(type(ver3))

"""single or double quotes is used to decleare a string in a variable"""
exmpl= "this is a string"
#is same as
exampl= 'this is a string'

"""variables names are case sensitive lower case a and upper case A is not same"""
a= "a veriable"
#is not same as
A="a different variable"

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""in python print() function is used to output variables.
In the print() function, you output multiple variables, separated by a comma.
also use the + operator to output multiple variables.
For numbers, the + character works as a mathematical operator.
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error
The best way to output multiple variables in the print() function is to separate them with commas, which even support different data type """

var1= "python is awesome"
print(var1)

var2= "you are "
var3= "so beautiful "
var4= "baba "
print(var2,var3,var4)
print(var2 + var3 + var4)
num1= 1
num2= 2
print(num1 + num2)
#if we try to add string and number together using + it will throw us error, so we use comma
print(var2, num2)

"""python global variables
Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value."""
x= "awesome" #global variable
def my_func():
    print("python is " + x)

my_func()

x= "amazing" #global variable
def func():
    x= "awesome" #local variable
    print("python is "+ x )
func()
print(x)

"""the global keyword...
If you use the global keyword, the variable belongs to the global scope.
To change the value of a global variable inside a function, refer to the variable by using the global keyword"""

def name():
    global x 
    x= "beautiful"
    print("you are so "+ x)
name()
print(x)


#python Math

