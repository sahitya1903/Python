# l=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(l,end=' ')
#         l+=1
#     print()

# l=[1,2,3,4,5,3,2,1,7,5,4,9]
# m=[]
# for i in l:
#     if i not in m:
#         m.append(i)
# print(m)

# l=[]
# for i in range(1,101):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         l.append(i)
# m=[]
# for i in range(1,101):
#     m.append(i**2)
# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):
#         if (l[i]+l[j]) in m:
#             print((l[i],l[j]),end=' ')

# l=input('Enter number:')
# c=0
# for i in range(len(l)-1):
#     b=int(l[i+1])-int(l[i])
#     if b==1:
#         c+=1
# print(c)


# a=(1,2,3,4,2,1,4,2,5,7,4,2,1)
# b=int(input('Enter element to search:'))
# for i in range(len(a)):
#     if a[i]==b:
#         print(i,end=',')

# # for i in range(1,6):
# #     print(' '*(5-i),end='')
# #     for j in range(1,2*i):
# #         print(j,end='')
# #     print()

# # n=int(input('Enter number of terms:'))
# # s=0
# # for i in range(1,n+1):
# #     s+=(i*(i+1)*(i+2))
# # print(s)

# # print('d'.upper())

# # l=[1,8,7,3,4,2]
# # for i in range(len(l)):
# #     for j in range(len(l)-1-i):
# #         if l[j]>l[j+1]:
# #             l[j],l[j+1]=l[j+1],l[j]
# #     print(l)

# l=[1,8,7,3,4,2]
# n=len(l)
# for i in range(n):
#     min=i
#     for j in range(i+1,n):
#         if l[j]<l[min]:
#             min=j
#     l[i],l[min]=l[min],l[i]
#     print(l)
# print(l)


# l=[1,8,7,3,4,2]
# for i in range(1,len(l)):
#     k=l[i]
#     j=i-1
#     while j>=0 and k<l[j]:
#         l[j+1]=l[j]
#         j-=1
#     else:
#         l[j+1]=k
#     print(l)
# print(l)

f=open('alpha.txt','w')
for i in range(65,91):
    f.write(chr(i)+'\n')
f.close()
f=open('alpha.txt')
s=f.readline()
c=0
while s:
    if s[0] in 'aeiouAEIOU':
        c+=1
    s=f.readline()
print(c)
f.close()