# a=input('Enter number to check:')
# b=int(a)
# s=0
# for i in range(len(a)):
#     s=s+int(a[i])**(i+1)
# if s==b:
#     print('Disarium')

# l=[]
# n=int(input('Enter no. of subjects:'))
# for i in range(n):
#     a=int(input('Enter marks:'))
#     l.append(a)
# max=l[0]
# min=l[0]
# for i in l:
#     if i>max:
#         max=i
# for i in l:
#     if i<min:
#         min=i
# s=0
# len=0
# for i in l:
#     len+=1
#     s=s+i
# avg=s/len
# c=-1
# for i in l:
#     c+=1
#     if i==max:
#         break
# d=-1
# for i in l:
#     d+=1
#     if i==min:
#         break
# print('max=',max)
# print('min=',min)
# print('avg=',avg)
# print('max index=',c,'min index=',d,end=' ')
# print('Sum of max and min index=', c+d)

# n=int(input('Enter rows:'))
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# n=int(input('Enter rows:'))
# for i in range(1,n+1):
#     print(' '*(n-i),'*'*i,end='')
#     print()

# n=int(input('Enter number:'))
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,2*i):
#         print(j,end='')
#     print()

# n=int(input('Enter number:'))
# a=65
# for i in range(1,n+1):
#     for j in range(a,i+a):
#         print(chr(j),end='')
#     print()

# for i in range(6):
#     print(' '*i,end='')
#     for j in range(6-i):
#         print('* ',end='')
#     print()

# n=int(input('Enter number of rows:'))
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         print('* ',end='')
#     print()
# x=int(input('Enter value of x:'))
# n=int(input('Enter number of terms:'))
# t=0
# s=0
# while t<n:
#     a=(-1)**t
#     b=x**t
#     c=a*b
#     s=s+c
#     t+=1
# print(s)

# r=int(input('Enter number of rows:'))
# for i in range(1,r+1):
#     print(' '*(r-i),end='')
#     for j in range(1,i+1):
#         print('* ',end='')
#     print()



# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.signal as sig
# # Generate time values
# t = np.linspace(-10, 10, 500)  # From -10 to 10 with 500 points

# # Compute the step function values
# y = np.where(t >= 0, 1, 0)

# # Plot the unit step function
# plt.figure(figsize=(8, 5))
# plt.plot(t, y, label='Unit Step Function', color='blue')
# plt.title('Unit Step Function')
# plt.xlabel('Time (t)')
# plt.ylabel('Amplitude')
# plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
# plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.legend()
# plt.show()

n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'* (2*i-1))