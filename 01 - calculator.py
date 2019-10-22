def addition(x, y):
    z = x + y
    print(x, '+', y, '=', z)
def subtraction(x, y):
    z = x - y
    print(x, '-', y, '=', z)


a1 = float(input('Enter first number: '))
symbol = input('+ / - ')
a2 = float(input('Enter second number '))

if symbol == '+':
    addition(a1,a2)
elif symbol == '-':
    subtraction(a1,a2)
else:
    print ('Enter valid symbol')