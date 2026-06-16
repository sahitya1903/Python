# # d={'dev':'yadav','nem':'chand','sakshi':'yadav'}
# # s={}
# # print(d.items())
# # print(d.values())
# # for i,j in d.items():
# #     print(i,j,end=' ')
# #     print()
# # Example 1: Splitting on whitespace
# sentence = "Hello world, this is a sample sentence."
# words = sentence.split()
# print(words)
# # Output: ['Hello', 'world,', 'this', 'is', 'a', 'sample', 'sentence.']

# # Example 2: Splitting with a specific separator
# date = "2022-01-01"
# date_parts = date.split('-')
# print(date_parts)
# # Output: ['2022', '01', '01']

# # Example 3: Limiting the number of splits
# sentence = "apple orange banana mango"
# fruits = sentence.split(' ', 2)
# print(fruits)
# # Output: ['apple', 'orange', 'banana mango']

# a={1:'sahitya',2:'Naveen'}
# print(a.values())
# print(a.items())
# print(a.keys())
# for i in a.values():
#     print(i)

# l=[1,2,3,4,5,6]
# x=2
# def search(beg,end,l,x):
#     while beg<=end:
#         mid=(beg+end)//2
#         if x>l[mid]:
#             beg=mid+1
#         elif x<l[mid]:
#             end=mid-1
#         else:
#             return mid
#     else:
#         return -1
# a=search(0,len(l)-1,l,x)
# if a==-1:
#     print('Element not found')
# else:
#     print('Index:',a)


# a='This is my phone'
# s=a.split()
# b=''
# for i in s:
#     b=b+i[0]
# print(b)

# import os
# print(os.listdir())
# print(os.getcwd())
# os.chdir("../")
# print(os.getcwd())

# print(os.listdir())
# os.listdir()

# n=int(input('Enter no. of rows:'))
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(i):
#         print('*',end='')
#     print()

# n=int(input('Enter no. of upper triangle rows:'))
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         print('* ',end='')
#     print()
# for i in range(1,n):
#     print(' '*i,end='')
#     for j in range(1,n+1-i):
#         print('* ',end='')
#     print()

# a=int(input('Enter number:'))
# b=int(input('Enter factor number:'))
# c=1
# for i in range(1,a+1):
#     if b<=a:
#         if a%i==0:
#             if c==b:
#                 print(f'{b}th factor: {i}')
#                 break
#             c+=1
# s=0
# for i in range(7):
#     s=s+7
#     print(s)
# for i in range(1,5):
#     print(' '*(5-i),'*'*i)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
# for i in range(5):
#     for j in range(i+1,0,-1):
#         print(j,end='')
#     print()

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
