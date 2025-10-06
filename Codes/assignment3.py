# #Q1
# l=eval(input('Enter a list of numbers:'))
# e=0
# o=0
# for i in l:
#     if i%2==0:
#         e+=1
#     else:
#         o+=1
# print('Even Numbers in list:',e)
# print('Odd numbers in list:',o)

# #Q2
# l1=eval(input('Enter list 1 of unique elements:'))
# l2=eval(input('Enter list 2 of unique elements:'))
# l=[]
# for i in l1:
#     for j in l2:
#         m=[i,j]
#         l.append(m)
# print(l)

# #Q3
# l=eval(input('Enter a list of numbers:'))
# k=int(input('Enter frequency:'))
# for i in l:
    


# #Q4                           #using list
# f=open('file.txt')
# s=f.read()
# l=s.split()
# max=1
# for i in l:
#     a=l.count(i)
#     if a>max:
#         max=a
# for i in l:
#     if l.count(i)==max:
#         print(i)
#         break

# #Q4                         #using dictionary
# f=open('file.txt')
# s=f.read()
# l=s.split()
# m={}
# for i in l:
#     if i not in m:
#         m.update({l.count(i):i})
# for j in m:
#     if max(m)==j:
#         print(m[j])


# #Q5
# n=int(input('Enter an integer:'))
# for i in range(2,n+1):
#     if n%i==0:
#         print(f'Smallest divisor of {n} (other than 1) is {i}.')
#         break

# # Q6
# print('Sample sequence is: 1/(2**s) + 1/(3**s) + 1/(5**s) + 1/(7**s) + 1/(11**s) + 1/(13**s) + ....')
# n=int(input('Enter number of terms in series:'))
# s=int(input('Enter power of denominator:'))
# l=[]
# for i in range(1,n**2):
#     c=0
#     for j in range(1,n**2):
#         if i%j==0:
#             c+=1
#     if c==2:
#         l.append(i)
# sum=0
# seq=''
# for i in range(n):
#     seq+=f'1/({l[i]}**{s})+'
#     sum+=1/(l[i]**s)
# print('Generated Sequence:',seq)
# print('Sum of sequence:',sum)
    
# #Q7
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# # c=a
# # a=b
# # b=c
# a=a+b
# b=a-b
# a=a-b
# print(f'First Number:{a} , Second Number:{b}')

# #Q8
# r=input('Enter roll number in digits:')
# a=int(r)
# b=''
# while a!=0:
#     d=a%2
#     a=a//2
#     b=str(d)+b
# print('Binary Format:',b)
# if b==b[::-1]:
#     print('True')
# else:
#     print('False')

# #Q13
# n=int(input('Enter a number:'))
# l=[]
# for i in range(1,n+1):
#     if n%i==0:
#         l.append(i)
# m=[]
# for i in l:
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c>2:
#         m.append(i)
# print('No. of non-prime factors:',len(m))

# #Q14
# def fib(n):
#     if n<=0:
#         return -1
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(9))

# #Q21
# f=open('file.txt')
# b=''
# s=f.readline()
# while s:
#     if len(s)>len(b):
#         b=s
#     s=f.readline()
# print(b)

# #Q22
# a=input('Enter comma separated values:')
# l=a.split(',')
# l.sort()
# for i in l:
#     print(i,end=',')

# #Q9
# print('''Sequence Sample:
# (a**1)*((x)**n)+ (a**2)*(x**(n-1)) + ....''')
# n=int(input('Enter no. of terms:'))
# a=int(input('Enter base value:'))
# x=int(input('Enter power value:'))
# sum=0
# seq=''
# for i in range(n,0,-1):
#     sum+=((a**(n-i+1))*(x**i))
#     seq+=(f"({a}**{n-i+1})*({x}**{i})+")
# print('Sequence:',seq)
# print('Sum:',sum)

l1=[1,2,3,7,9]
l2=[1,4,6,8,10]
k=int(input('Enter number of pairs:'))
l=[]
for i in l1:
    for j in l2:
        s=i+j
        l.append(s)
l.sort()
m=l[:k]
for i in l1:
    for j in l2:
        s=i+j
        if s in m:
            print(i,j,end='     ')