# len()
# c=0
# l=[1,3,5,7,8]
# for i in l:
#     c+=1
# print('Length of sequence is:',c)

#remove() function in list
l=eval(input('Enter list with square brackets:'))
m=[]
a=eval(input('Enter element to remove:'))
for i in l:
    if i==a:
        a=None
    else:
        m.append(i)
print(m)

a=int(input('Enter number:'))
c=0
while a>0:
    c+=1
    a=a//10
print('Total digits of number are:',c)

a=int(input('Enter value of the base:'))
b=int(input('Enter value of the power to which the base is raised:'))
c=1
if a==0 and b==0:
    print('The operation value is NOT DEFINED')   
else:
    for x in range(b):
        c=c*a
    print('The value of given operation is:',c)