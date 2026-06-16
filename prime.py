a=int(input('Enter the number you want to check:'))
c=0
for i in range(1,a+1):
    if a%i==0:
        c+=1
if c==2:
    print('The number is prime.')
elif c>2:
    print('The number is composite.')
else:
    print('The number is neither prime nor composite.')

d=0
e=0
while True:
    a=int(input('Enter number:'))
    if a!=-1:
        c=0
        for i in range(1,a+1):
            if a%i==0:
                c+=1
        if c==2:
            d+=1
        elif c>2:
            e+=1
    else:
        print('The no. of prime numbers is:',d)
        print('The no. of composite numbers is:',e)
        break

a=int(input('Enter the starting value of prime number range:'))
b=int(input('Enter the end value of the prime number range:'))
for x in range(a,b):
    c=0
    for y in range(1,x+1):
        if x%y==0:
            c+=1
    if c==2:
        print(x,end=' ')