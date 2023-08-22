x= float(input('enter first number: ')) #taking first input
y= float(input('enter second number: ')) #taking second input
z= input('mention operator: ') #taking operator input

def result():
    if z == '+' or z == 'plus':
        return(x + y)
    elif z == '-' or z == 'minus':
        return(x - y)
    elif z == '*' or z == 'multiply':
        return(x * y)
    elif z == '/' or z == 'division':
        return(x / y)
    elif z == '**' or z == '^':
        return(x ** y)
    elif z == '%':
        return(x % y)
    else:
        print('unknown operator')

re= result() #storing the output inside a variable
result = str(re) #converting output into string
print(str(x), str(z), str(y), '=', result)