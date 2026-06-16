i=int(input('Enter number of terms in the Fibonacci Series:'))
a=0
b=1
if i<=0:
    pass
elif i==1:
    print(a)
elif i==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for x in range(i-2):
        c=a+b
        a=b
        b=c
        print(c)

i=int(input('Enter number of terms in the Fibonacci Series:'))
a=0
b=1
if i<=0:
    pass
elif i==1:
    print(a)
elif i==2:
    print(b)
else:
    for x in range(i-2):
        c=a+b
        a=b
        b=c
    print(c)