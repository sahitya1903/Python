print('****Welcome to Quadratic Equation Solver****')
print('''A quadratic equation is of form ax²+bx+c. Enter values of a, b and c corresponding to the given equation.''')
while True:
    a=float(input('Enter value of a:'))
    b=float(input('Enter value of b:'))
    c=float(input('Enter value of c:'))
    D=(b**2)-(4*a*c)
    x=D**0.5
    if D>0:
        print('The equation has 2 real and distinct roots.')
        p=(-b-x)/(2*a)
        q=(-b+x)/(2*a)
        print('The two roots of the given equation are: p=',p,'and q=',q,'.')
    elif D==0:
        print('The equation two real and equal roots.')
        p=-b/(2*a)
        print('The two roots of the equation are: p=',p,'and q=',p,'.')
    else:
        print('The equation has no real roots.')
    i=input('Do you want to solve more equations? Enter (Y/y/N/n)..')
    if i in 'Nn':
        break
    else:
        print('Invalid input..')