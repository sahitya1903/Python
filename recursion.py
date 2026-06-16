def fibo(n):
    if n<0:
        print('Invalid no. of terms')
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input('Enter no. of terms:'))
for i in range(n):
    print(fibo(i))

def fact(n):
    if n<0:
        print('Factorial not possible..')
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input('Enter number for factorial:'))
print('Factorial is:',fact(n))

# def sum(n):
#     if n<0:
#         print('Invalid no. of terms')
#     elif n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# num=int(input('Enter number of natural numbers from the start:'))
# print(f'Sum of first {num} natural numbers is: {sum(num)}')

# def prod(a,b):
#     i=b
#     while i!=0:
#         i-=1
#         return a+prod(a,i)
#     else:
#         return 0
# print(prod(5,3))

# a=int(input('Enter number:'))
# c=0
# def num(a):
#     global c
#     if a<0:
#         print('Invalid number entered.')
#     elif a>0:
#         a=a//10
#         c+=1
#         return num(a)
#     else:
#         return c
# print(num(a))

def gcd(a, b):
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)

a = 25
b = 45
print(gcd(a, b))