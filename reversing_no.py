
a=input('Enter a number for reversing:')
b=int(a)
for i in range(len(a)):
    c=b%10
    b=b//10
    print(c,end='')

a=int(input('Enter a number to reverse:'))
s=0
while a>0:
    d=a%10
    s=s*10+d
    a=a//10
print(s)