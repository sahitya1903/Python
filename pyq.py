
a=int(input('How many integers?'))          #q2
l=[]
m=[]
s=0
p=0
q=0
i=0
while i<a:
    b=int(input('Next Integer?'))
    s=s+b
    if b%2==0:
        p=p+b
        l.append(b)
    else:
        q=q+b
        m.append(b)
    i+=1
print('Total Sum=',s)
print('Even Sum=',p)
print('Odd sum=',q)
print('Even max=',max(l))
print('Odd max=',max(m))


a=input('Enter a 12 digit number:')         #q5
c=0
d=0
for i in range(12):
    if i%2==0:
        c=c+int(a[i])*1
    else:
        d=d+int(a[i])*3
s=c+d
t=s%10
print(int(a),t,sep='')



rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):               # Print spaces
        print(" ", end="")
    for k in range(1, 2*i):                 # Print numbers
        print(k, end="")
    print()                                 # Move to the next line after each row

a=input('enter a number:')
b=int(a)
c=0
for i in range(len(a)):
    d=int(a[i])**(i+1)
    c=c+d
if c==b:
    print('The given no. is Diasarium number')
else:
    print('Given no. is not diasarium number')

import math                             #cos()
n=int(input('Enter number of terms:'))
x=float(input('Enter value of x:'))
c=0
p=0
while c<=n:
    a=(-1)**c
    b=(x**(2*c))/math.factorial(2*c)
    d=a*b
    p=p+d
    c=c+1
print(p)