l=eval(input('Enter list:'))
k=int(input('Enter min length of sublist (min not included):'))
s=int(input('Enter min sum of elements:(min not included)'))
l.sort()
l.reverse()
c=0
m=[]
for i in l:
    c=c+i
    m.append(i)
    if c>s and len(m)>k:
        print(m)
        break

# n=int(input('Enter number of strings:'))
# l=[]
# for i in range(n):
#     a=input('Enter string of alphabets:')
#     l.append(a)
# for i in l:
#     c=0
#     for j in range(len(i)-1):
#         if i[j]==i[j+1]:
#             c+=1
#     print(f'String={i},Deletions={c}')

'''f=open('input.txt')          #ERROR
s=f.read()
l=s.split()
c=0
for i in range(len(l)):
    for j in range(len(l[i]-1)):
        if l[i][j]==l[i+1][j]:
            c+=1
print(c)'''


# for i in range(5):
#     print(' '*(5-i),end='')
#     for j in range(i,-1,-1):
#         print(j,end='')
#     if i!=0:
#         for k in range(1,i+1):
#             print(k,end='')
#     print()

# n=int(input('Enter terms:'))
# for i in range(2,n+2):
#     for j in range(1):
#         print(f"{'0,'*(i-2)}{i-2},{i-1},",end='')

n=int(input('Enter order of matrix:'))
l=[]
for i in range(1,n+1):
    print(f'Element for {i} row')
    m=[]
    for j in range(1,n+1):
        a=int(input(f'Enter element for ROW {i} and COLUMN {j}:'))
        m.append(a)
    l.append(m)
print('Matrix:',l)
for i in l:
    print(i)
