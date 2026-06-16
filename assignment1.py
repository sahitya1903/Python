#Q1

x=float(input('Enter distance travelled on the first day:'))
y=float(input('Enter the distance needed to be travelled before the event:'))
c=1
while x<y:
    x=x+0.1*x
    c=c+1
print(f'The no. of days needed to complete distance {y} are:',c)

#Q2
# s=''
# c=0
# while True:
#     a=input('Enter element:')
#     if a!='0':
#         s=s+a+'\n'
#         c+=1
#     else:
#         print(s)
#         print('Length of sequence is:',c)
#         break

c=0
while True:
    a=int(input('Enter a number:'))
    if a==0:
        print('Length of sequence is:',c)
        break
    c+=1

#Q3
sum=0
while True:
    a=int(input('Enter element:'))
    if a!=0:
        sum=sum+a
    else:
        break
print('Sum of the sequence is:',sum)

#Q4

# l=[]
# while True:
#     a=int(input('Enter element:'))
#     if a!=0:
#         l.append(a)
#     else:
#         print('The sequence of integers is:',l)
#         break
# print('The index number of maximum number is:',l.index(max(l)))

l=[]
while True:
    a=int(input('Enter element:'))
    if a!=0:
        l.append(a)
    else:
        break
max=l[0]
for i in l:
    if i>max:
        max=i
c=0
for i in range(len(l)):
    if l[i]==max:
        print(c)
        break
    c+=1

#Q5

n=int(input('Enter a number whose factor you want to find:'))
m=int(input('Enter the serial no. of the factor:'))
i=1
c=0
while n>=m and i<=n:
    if n%i==0:
        c+=1
        if c==m:
            print(f'The {m}th factor of {n} is:',i)
            break
    i=i+1
else:
    print('Factor serial number is beyond the number of factors.')