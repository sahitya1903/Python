print('****Welcome to your Calculator application****')
a=float(input('Enter first number:'))
b=float(input('Enter second number:'))
s=a+b
d=a-b
p=a*b
q=a/b
f=a//b
r=a%b
e=a**b
def calc():
    print('''Enter operation you want to perform:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Floor Division
        6. Remainder
        7. Exponent''')
    n=int(input('Enter your choice:'))
    if n==1:
        print(s)
    elif n==2:
        print(d)
    elif n==3:
        print(p)
    elif n==4:
        print(q)
    elif n==5:
        print(f)
    elif n==6:
        print(r)
    elif n==7:
        print(e)
    else:
        print('Invalid Operation')
calc()
while True:
    i=input('Do you want to perform any other operations? Enter (Y/y/N/n):')
    if i=='Y' or i=='y':
        calc()
    elif i=='N' or i=='n':
        print('****Have a nice day****')
        break
    else:
        print('Invalid Operation')
        break

