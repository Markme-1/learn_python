#string in python
#creation

var1='i am a learning python' #this is string a set of characters

# print function is being used to view the string 
print(var1)
print('this is a string')
print("this is another string")

#a string should always write inside a single quotetion or double quotetion

print("""this is a
multi line string""") #triple quote fro multi line string.

print('\n') #\n is use to create a new line
print('test that new line out')



#Accessing characters
""" accessing individual character inside a string can be done through indexing. starting from 0. space between string also count"""
print(var1[2])

#String Concatenation:
"""it is possible to join two or multiple strings using '+' """
var2= 'the topic is string'
print(var1 + " " + var2)

#string length
"""using the len() function it is possible to determine the length of the string"""

length = str((len(var1)))
print("the length is " + length)

print(len(var2))

#string slicing
"""it is possible to extract a substring from a string using slicing, by mentioning the start and end indices"""

mystring= var1[16:22]
print(mystring)

#string method
"""Python provides various built-in methods to manipulate and transform strings. Examples include upper(), lower(), strip(), split(), replace(), and more."""

print(mystring.upper())

#string formatting 
"""String formatting allows you to embed values within a string. This can be done using the % operator or the format() method."""

Name= 'Alice'
age= 30
print('my name is %s and age is %d' % (Name, age))

print('\n')

#Math

#math using python

#math operators 

a= 10
b=2

print(a + b) #add
print(a - b) #substract
print(a * b) #multiple
print(a / b) #division
print(11 % 2) #modulo/reminders
print(11 // 2) #Performs division and returns the quotient as an integer (rounds down)
print(10 ** 2) #raise a number to a power

import math #importing math module for advance mathematical operations

print(math.exp2(2)) #raise a number using power 2 value.

print('\n')

#Variables & Methods

"""variables are like a storage where a string/int/float is stored"""

var3= 'this is my python lession'

print(var3)
print(var3.upper()) #uppercase
print(var3.lower()) #lowercase
print(var3.title()) #title
print(len(var3)) #count the character

var4= 'bob'
age= 30
cgp= 8.0

print('the user name is ' + var4, 'user age is ' + str(age))

age += 1
print(age)

print('\n')

#Function
def func(): #this is a function without parameter
    x= 'this is a function' #local variable
    print(x)
func()

def number(num): #function with parameter
    print(num + 100)
number(100) #passing a parameter

def add(x,y):
    print(x + y)
add(2,2)

def sub(x,y):
    return(x - y) #return will not show the output it will store the output and later after using the print statement it shows output
print(sub(4,3))

x= 'function' #global variable
def fun():
    print('beautiful ' + x)
fun()
print(x)

def newline(): #newline function
    print('\n')
newline()


#relational operators

#python provides several relational operators to compare values.

x= 5
y= 7

print(x == y)#compare both values are equals
print(x != y)#compare both values are not equal
print(x > y)#checks if left value is grater than right value
print(x < y)#checks if right value is grater than left falue
print(x >= y)#checks if left value is grater than or equals to right value
print(x <= y)#checks if right value is grater than or equals to left value

newline()

#boolean expression
#Boolean expressions are formed by combining relational expressions using logical operators. The logical operators in Python are

"""
Logical AND (and): Returns True if both operands are True.
Logical OR (or): Returns True if at least one operand is True.
Logical NOT (not): Negates the value of the operand.

"""
w= 10
x= 5
y= 6
z= 5

print(x > y or x > w)
print(x == z and x > y)
print(not(x == z))

newline()

#conditional statement [if/else statement]

def drink(money):
    if money >= 20:
        return "you can buy the drink"
    else:
        return "you cannot buy the drink"
print(drink(20))
print(drink(19))


def alcohol(age,money):
    if (age >= 20) and (money >= 20):
        print ("you can have the drink")
    elif (age >= 20) and (money != 20):
        print("you don't have enough money to buy")
    elif (age != 20) and (money >= 20):
        print("you are too young to buy")
    else:
        print("bye bye")
alcohol(30,30)
alcohol(25,19)
alcohol(19,30)
alcohol(18,12)

newline()

#list
#list defines using [] and it is changable

mylist= ['dodge', 'lamborghini', 'Range Rover', 'nissan', 'mitsubishi']
print(mylist)
print(mylist[0])#using indexing with list. indexing start with 0
print(mylist[0:3])#it will show the output till index 3 but not index 3. known as slicing
mylist.append('honda') #addsomething at the end of the list
print(mylist)
mylist[5]= 'aston martin' #add/replace something on a list using a index number
print(mylist)
mylist.append('suzuki')
print(mylist)
mylist.remove('suzuki')
print(mylist)

ntherlist= ['volkswagan', 'ford', 'toyota']

newlist= mylist + ntherlist #add multiple list
print(newlist)
print(len(newlist)) #total iteams inside a list


#2D list

grade= [['bob',80], ['alice',75], ['jan', 70]]
print(grade)
print(grade[2:4])

#tuples
#do not change ()

fruits= ('apple', 'banana', 'greps')
print(fruits[1])
#same as lists but touples are not changeable

newline()

#looping
#for loop - start to finish of an iterate

x= ('me', 'myself', 'i')

for tupple in x:
    print(tupple)

#while loop- execute as long as true
x= 1
while x < 10:
    print(x)
    x += 1

"""The break and continue Statements:

Within loops, you can use the break statement to exit the loop prematurely and the continue statement to skip the current iteration and move to the next one."""

newline()

#advanced string
"""In Python, the str (string) data type represents a sequence of characters enclosed within 
single quotes (' ') or double quotes (" ").Strings in Python are immutable, which means they cannot be
changed after they are created. Here are some key points about strings in Python"""

my_string= 'Hello World!'

print(my_string[0]) #Accessing Character
print(len(my_string)) #string length
print(my_string[1:4]) #slicing string
print(my_string.upper()) #string methods
print(my_string.split()) #delimeter default is space

string= "this is a string"
string_split= string.split()
print(string_split)
string_join= ' '.join(string_split)
print(string_join) 

quote= "he said, 'give me all your money'" #if we want to use quote inside quote
print(quote)
quote= "he said \"give me all your money\" " #or we can use escape character
print(quote)

#diffferent types to join strings
movie= 'fast and furious'
print("i love to watch: " + movie)
print("i love to watch {}" .format(movie))
print("i love to watch %s" % movie)
print(f"i love to watch {movie}")

newline()

#dictionary
#it represent using {}. dictionary is a key/value pair

dictionary= {'banana': 5, 'apple': 3, 'strawberry': 7} #banana is key and 5 is value
print(dictionary)
dictionary['banana']= 7 #update single key
print(dictionary)
print(dictionary.get('apple'))#return the value of key
employees= {'sales': ['joy', 'ravi', 'sakshi'], 'IT': ['abhi', 'roy']}
print(employees)
employees['marketting']= ['joye', 'chandler'] #updating dictionary
print(employees)
employees.update({'finance': ['viru', 'rijo']})#updating dictionary
print(employees)

