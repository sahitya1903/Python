# Q1
print('The notes available are of denomination Rs.10, 50 and 100 only.')
a=int(input('Enter the amount to be withdrawn in multiples of 10:'))
def amount(a):
    h=a//100
    a=a%100
    f=a//50
    a=a%50
    t=a//10
    print(f'Rs.100 notes:{h}, Rs.50 notes:{f}, Rs.10 notes:{t}')
amount(a)

# Q2
d=int(input('Enter number of days late for returning book:'))
def days(d):
    if  d>0 and d<=30:
        s=0
        for i in range(1,d+1):
            if i<=5:
                s=s+0.5
            elif i>5 and i<=10:
                s=s+1
            elif i>10 and i<=30:
                s=s+5
        print('Fine for late book submission is:',s)
    else:
        print('Sorry, Your Library Membership is cancelled')
days(d)

# Q3
l=eval(input('Enter a list of numbers:'))
m=tuple(l)
l.sort()
n=tuple(l)
print(m,n)
def is_sorted(l):
    if m==n:
        return True
    else:
        return False
print(is_sorted(l))

# Q4
a=input('Enter first string:')
b=input('Enter second string:')
def first_diff(a,b):
    if len(a)>len(b):
        a,b=b,a
    else:
        for i in range(len(a)):
            if a[i]!=b[i]:
                print('First location:',i,end=' ')
                break
    if a==b:
        print('-1')
first_diff(a,b)

# Q5
l=eval(input('Enter a list of distinct numbers:'))
l.sort()
m=[]
def thrice(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]%l[i]==0 and i!=j:
                if l[i] not in m:
                    m.append(l[i])
    return m
print('The numbers which have their multiples in same list are:',thrice(l))
