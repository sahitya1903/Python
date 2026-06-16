l=[1,2,3,4,1,5,6,1,3,2,1,6,2,3,6]
m=[]
for i in l:
    if i not in m:
        m.append(i)
print(m)

n=[]
for i in m:
    if l.count(i)>1:
        t=(i,l.count(i))
        n.append(t)

print('Duplicate elements along with their occurence are:',n)