# d={1:'sk',2:[1,2]}
# l=[]
# for i in d.items():
#     l.append(i)
# print(l)
# d.update({3:'sss'})
# print(d)
# d.clear()
# print(d)

# n=int(input('Enter no. of elements in dictionary:'))
# d={}
# for i in range(n):
#     k=eval(input('Enter key:'))
#     v=eval(input('Enter value:'))
#     s={k:v}
#     d.update(s)
# print(d)

d={}
d[1]='s'
d[2]='k'
print(d.get(1))
# s={}
# s[3]='m'
# s[4]='d'
# d.update(s)
# print(d)

d={1:'s',2:'k'}
s=d.copy()
print(id(d))
print(id(s))
s.update({3:'n',4:'m'})
print(d)
print(s)