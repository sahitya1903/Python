#Q1(a)

n=int(input('Enter number of terms in sequence:'))
p=1
s=0
a=''
for i in range(1,n+1):
    p=p*i
    a= a+ f'({i}/{i}!)'
    if i!=n:
        a=a+'+'
    s=s+(i/p)
print('The sequence is:',a)
print('The sum of sequence is:',s)

#Q1(b)

n=int(input('Enter no. of terms in sequence:'))
a=3
if n<=0:
    print('None..')
elif n==1:
    print(a)
else:
    print(a,end=',')
    for i in range(2,n+1):
        b=a*5+5
        print(b,end=',')
        a=b

#Q2

a=input('Enter binary or octal number:')
b=int(a)
c=int(input('Enter base:'))
s=0
for i in range(len(a)):
    if c==2 and a[i] in '01':
        d=b%10
        s=s+d*(2**i)
        b=b//10
    elif c==8 and a[i] in'01234567':
        e=b%10
        s=s+e*(8**i)
        b=b//10
    else:
        print('The number is neither in binary nor in octal format.')
        break
print('The decimal value is:',s)

#Q3

a=input('Enter a decimal number:')
b=int(a)
c=int(input('Enter base for conversion:'))
s=''
while b!=0:
    if c==2:
        d=b%2
        s=str(d)+s
        b=b//2
    elif c==8:
        d=b%8
        s=str(d)+s
        b=b//8
    else:
        print('Only binary and octal conversions are supported.')
        break
print(s)

#Q4

a=input('Enter a hexadecimal number:')
d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
s=0
b=a[::-1]
for i in range(len(b)):
    if b[i] in d:
        c=d[b[i]]
        s=s+c*(16**i)
    else:
        print('The number you entered is not in hexadecimal number format.')
        break
print(s)

#Q5

a=int(input('Enter a number:'))
for i in range (2,a+1):
    if a%i==0:
        print('The least divisor of no. is:',i)
        break

