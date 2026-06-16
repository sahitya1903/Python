# a=input('Enter number to check for armstrong number:')
# b=int(a)
# c=0
# for i in range(len(a)):
#     c=c+(int(a[i])**len(a))
# if b==c:
#     print('No. is armstrong.')       

a=int(input('Enter number:'))
b=a
l=0
while a>0:
    l+=1
    a=a//10
s=0
c=b
while b>0:
    d=b%10
    s=s+d**l
    b=b//10
if s==c:
    print('Armstrong number')
