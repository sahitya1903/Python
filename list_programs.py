l=[1,2,-2,5,6,-5,-9,3,6]
for i in range(len(l)-1):
    if (l[i]>0 and l[i+1]>0) or (l[i]<0 and l[i+1]<0):
        print([l[i],l[i+1]])

c=0
l=[1,4,5,3,7,2,0,8]
for i in range(len(l)-1):
    if (l[i]>l[i+1]) and l[i]>l[i-1]:
        c+=1
        print(l[i])
print('The no. of elements greater thean neighbours is:',c)

l=[2,3,4,1,1,3,2,5,7,8,5,3]
l.sort()
print(l)
c=0
for i in l:
    if l.count(i)==1:
        c+=1
print('No. of distinct elements in the given list are:',c)

l=[1,2,3,4,5,0,8,3,2,2,1,5,4]
m=[]
for i in l:
    if l.count(i)==1:
        m.append(i)
print(m)

l=[1,2,3,4,5,8,7,6,10,9]
m=[]
c=l.index(max(l))
d=l.index(min(l))
for i in range(len(l)):
    if i!=c and i!=d:
        m.append(l[i])
    elif i==c:
        m.insert(i,min(l))
    else:
        m.insert(i,max(l))
print(m)

l=[1,2,3,4,5,6,7,8,9,10]
i=0
n=len(l)-1
while i<(len(l)/2):
    sum=l[i]+l[n]
    print(sum)
    i+=1
    n-=1           

l=[1,2,3,4,5,3,2,1,3,7,6]
m=[]
for x in l:
    if x not in m:
        m.append(x)
for i in m:
    if l.count(i)>1:
        for j in range(len(l)):
            if l[j]==i:
                print(f'The index of duplicate element {i} is {j}')
        print() 

l=[]
max=0
while True:
    a=int(input('Enter element:'))
    if a==0:
        break
    else:
        l.append(a)
        if a>max:
            max=a
for i in range(len(l)):
    if l[i]==max:
        print(i)