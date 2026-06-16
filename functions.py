a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(f'The maximum of given three numbers is:{max(c,max(a,b))}')


l=eval(input('Enter a list of numbers:'))
max=l[0]
c=0
for i in l:
    if i>max:
        max=i
for i in l:
    if l[i]==max:
        c+=1
print(f'Maximum number in list: {max},Occurence:{c}')



# n=int(input('Enter number for finding factorial:'))
# def fact(n):
#     p=1
#     for x in range(1,n+1):
#         p=p*x
#     print(f'The factorial of {n} is: {p}')
# fact(n)

# n=int(input('Enter no. of terms of Fibonacci series:'))
# def fibo(n):
#     a=0
#     b=1
#     if n<=0:
#         print('Enter correct no. of terms:')
#     elif n==1:
#         print(a)
#     elif n==2:
#         print(a)
#         print(b)
#     else:
#         print(a)
#         print(b)
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(c)
#         print(f'The {n}th term of fibonacci series is: {c}')
# fibo(n)


# def maximum(a,b,c):
#     if a>=b and a>=c:
#         print(a,'is greatest')
#     elif b>=a and b>=c:
#         print(b,'is greatest')
#     elif c>=a and c>=b:
#         print(c,'is greatest')
# maximum(2,3,5)

def listsum(l):
    s=0
    for i in l:
        s=s+i
    print('Sum is:',s)
l=eval(input('Enter list of numbers:'))
listsum(l)

n=int(input('Enter number to check for perfect number:'))
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if n==s:
        print('Perfect Number')
perfect(n)

l=eval(input('Enter list of numbers:'))
def func(l):
    m=[]
    for i in l:
        if l.count(i)==1:
            m.append(i)
    print(m)
func(l)
    
# def hcf(a,b):
#     if a>b:
#         a,b=b,a
#     else:
#         while True:
#             c=b%a
#             if c==0:
#                 print(f'HCF is:{a}')
#                 break
#             b=a
#             a=c
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# hcf(a,b)

# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# c=int(input('Enter third number:'))
# l=[a,b,c]
# l.sort()
# a,b,c=l[0],l[1],l[2]
# def hcf(a,b,c):
#     while True:
#         d=b%a
#         if d==0:
#             break
#         b=a
#         a=d
#     while True:
#         f=c%a
#         if f==0:
#             print(f'HCF is {a}')
#             break
#         c=a
#         a=f
# hcf(a,b,c)



# p=int(input('Enter first number:'))
# q=int(input('Enter second number:'))      ###ERROR HCF NONE
# r=int(input('Enter third number:'))
# def hcf(a,b):
#     if a>b:
#         a,b=b,a
#     else:
#         while True:
#             c=b%a
#             if c==0:
#                 return a
#             b=a
#             a=c
# print('HCF is:',hcf(r,hcf(p,q)))