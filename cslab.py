'''
Submitted by: Sahitya Kushwaha
Reg. No.: 9232440
Class: BTech I
Sec: H
'''




#Q1. To book tickets and print fare.

print('****Welcome to Book My Tickets App..****')
a=int(input('Enter the number of Tickets you want to purchase:'))
b=300
tot=a*b
print('Your total bill is',tot)





#Q2. To print a statement “My age is…..”

a=int(input('Enter age:'))
print('My age is:',a)





#Q3. Print greatest number among two numbers.

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
if a>b:
    print(a,'is greater')
elif a==b:
    print('Both a and b are equal to', a)
else:
    print(b,'is greater')





#Q4. Print greatest number among three numbers.

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
if (a>=b and a>=c):
    print(a,'is greatest')
elif (b>=a and b>=c):
    print(b,'is greatest')
else:
    print(c,'is greatest')





#Q5. Check whether the number is even or odd

a=int(input('Enter number to check:'))
if a%2==0:
    print('Even Number')
else:
    print('Odd number')





#Q6.Program which suggests the user to do exercise according to a day.

print('''The list of days is given as:
1.Monday 2.Tuesday 3.Wednesday 4.Thursday 5.Friday 6.Saturday 7.Sunday''')
a=int(input('Enter your choice as day number:'))
if a==1 or a==4:
    print("Today's task is Jogging.")
elif a==2 or a==5:
    print("Today's task is Running.")
elif a==3 or a==6:
    print("Today's task is Yoga.")
elif a==7:
    print("It's Sunday today. Take a rest.")
else:
    print('Invalid operation..')





#Q7. To implement Grading system

print('Welcome to avg and percentage calculator:')
a=float(input('Enter your marks out of 100 in first subject:'))
b=float(input('Enter your marks out of 100 in second subject:'))
c=float(input('Enter your marks out of 100 in third subject:'))
d=float(input('Enter your marks out of 100 in fourth subject:'))
e=float(input('Enter your marks out of 100 in fifth subject:'))
f=float(input('Enter your marks out of 100 in sixth subject:'))
avg=(a+b+c+d+e+f)/6
print('Your avg marks are',avg)
if (a>=35 and b>=35 and c>=35 and d>=35 and e>=35 and f>=35):
    if avg>80 and avg<=100:
        print('You are awarded Excellent grade.')
    elif avg>70 and avg<=80:
        print('You are awarded A grade.')
    elif avg>60 and avg<=70:
        print('You are awarded B grade.')
    elif avg>50 and avg<=60:
        print('You are awarded C grade.')
    elif avg>40 and avg<=50:
        print('You are awarded D grade.')
    elif avg>=35 and avg<=40:
        print('You are awarded P grade.') 
    else:
            print('Incorrect values of marks is entered')
else:
     print('You have failed the examination. You are awarded F grade')





#Q8. To find out even numbers in a given range

for x in range(1,10):
    if x%2==0:
        print(x)





#Q9. To find out odd numbers in a given range

for x in range(1,10):
    if x%2!=0:
        print(x)





#Q.10 To print alternate numbers in a range

for x in range(1,10,2):
    print(x)





'''
Q.11 To take inputs starting and the ending values 
and print numbers between the starting and ending values.
'''

a=int(input('Enter starting value:'))
b=int(input('Enter end value:'))
for x in range(a,b+1):
    print(x)





#Q.12 To calculate and print sum of ‘n’ numbers from 0 to n (both inclusive)

a=int(input('Enter the number till which you want to calculate the sum:'))
s=0
for x in range(a+1):
    s=s+x
print('The sum is:',s)
d=(a**2+a)/2
if s==d:
    print('The values are checked and verified as correct.')





#Q.13 To calculate and print sum of squares of ‘n’ numbers from 0 to n (both inclusive)

a=int(input('Enter the end value till which you want sum of squares:'))
s=0
for x in range(0,a+1):
    s=s+pow(x,2)
print('The sum of squares upto end value is:',s)
d=(2*pow(a,3)+3*pow(a,2)+a)/6
if s==d:
    print('The values are checked and verified as correct.')





#Q.14 To calculate and print sum of squares of ‘n’ numbers from 0 to n (both inclusive)

a=int(input('Enter the end value till which you want to find the sum of cubes:'))
s=0
for x in range(0,a+1):
    s=s+x**3
print('The sum of cubes upto end value is:',s)
d=(a**4+2*a**3+a**2)/4
if s==d:
    print('The values are checked and verified as correct.')





#Q.15 To implement power function (without exponential operator) 

a=int(input('Enter value of the base:'))
b=int(input('Enter value of the power to which the base is raised:'))
c=1
if a==0 and b==0:
    print('The operation value is NOT DEFINED')   
else:
    for x in range(b):
        c=c*a
    print('The value of given operation is:',c)





#Q.16 Check whether the given number is prime or composite

a=int(input('Enter the number you want to check:'))
c=0
for i in range(1,a+1):
    if a%i==0:
        c+=1
if c==2:
    print('The number is prime.')
elif c>2:
    print('The number is composite.')
else:
    print('The number is neither prime nor composite.')





#Q.17 To print prime numbers in a given range

a=int(input('Enter the starting value of prime number range:'))
b=int(input('Enter the end value of the prime number range:'))
for x in range(a,b):
    c=0
    for y in range(1,x+1):
        if x%y==0:
            c+=1
    if c==2:
        print(x,end=' ')





'''
Q.18 As a future athlete you just started your practice for an upcoming event.
Given that on the first day you run x miles and by the event you must be able to
run y miles. Calculate the no. of days required for you to finally reach
the required distance for the event, if you increase your distance each day
by 10% from the previous day.
'''

x=float(input('Enter distance travelled on the first day:'))
y=float(input('Enter the distance needed to be travelled before the event:'))
c=1
while x<y:
    x=x+0.1*x
    c=c+1
print(f'The no. of days needed to complete distance {y} are:',c)





'''
Q.19 Given a sequence of non-negative integers where each no. is written
in a separate line. Determine the length of the sequence, where the sequence ends 
when the integer is equal to 0. Print the length of sequence (not counting 0).
The numbers following the number 0 should be omitted.
'''

c=0
while True:
    a=int(input('Enter a number:'))
    if a==0:
        print('Length of sequence is:',c)
        break
    c+=1





#Q.20 Determine sum of all elements in a sequence, ending with 0.

sum=0
while True:
    a=int(input('Enter element:'))
    if a!=0:
        sum=sum+a
    else:
        break
print('Sum of the sequence is:',sum)





'''
Q.21 A sequence consists of integers and ends with 0.
Determine the index of the largest element of the sequence.
If the highest element is not unique, print the index of first of them.
'''

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





#Q.22  To find mth factor of given number n.

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





#Q.23 To print n natural numbers in descending order.

a=int(input('Enter the starting value from which descending order starts:'))
while a>0:
    print(a)
    a=a-1





#Q.24 To print factorial of a given no. n

a=int(input('Enter the number whose factorial you want to find:'))
p=1
if a<0:
    print('Factorial not possible')
elif a==0:
    print('The factorial of 0 is: 1')
else:
    for x in range(1,a+1):
        p=p*x
    print('The value of factorial of entered number is:',p)





#Q.25 To display first 7 multiples of 7.

s=0
for i in range(7):
    s=s+7
    print(s)





#Q.26 To reverse a number.

a=int(input('Enter a number to reverse:'))
s=0
while a>0:
    d=a%10
    s=s*10+d
    a=a//10
print(s)





'''
Q.27 To print following pattern:
*
**
***
****
*****
'''

for i in range(1,6):
    print('*'*i)





'''
Q.28 To print following pattern:
    *
   **
  ***
 ****
*****
'''

for i in range(1,6):
    print(' '*(n-i),'*'*i)





'''
Q.29 To print following pattern:
1
12
123
1234
12345
'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()





'''
Q.30 To print following pattern:
    1
   21
  321
 4321
54321
'''

for i in range(5):
    for j in range(i+1,0,-1):
        print(j,end='')
    print()





#Q.31 To find whether a number is Armstrong or not.

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





#Q.32 To find whether a number is palindrome or not.

a=int(input('Enter number to check for palindrome:'))
n=a
s=0
while a>0:
    c=a%10
    s=s*10+c
    a=a//10
if n==s:
    print('Palindrome')





#Q.33 To count the total number of digits in a number using a while loop.

a=int(input('Enter number:'))
l=0
while a>0:
    l+=1
    a=a//10
print('No. of digits in number:',l)





'''
Q.34 To print following pattern:
54321
4321
321
21
1
'''

for i in range(5):
    for j in range(5-i,0,-1):
        print(j,end='')
    print()





#Q.35 To display numbers from -10 to -1 (both inclusive) using for loop

for x in range(-10,0):
    print(x)





'''
Q.36 Write a program to calculate the sum of series up to n terms.
For example, if n =5 the series will become:
2 + 22 + 222 + 2222 + 22222 = 24690
'''

n=int(input('Enter number of terms in series:'))
s=0
c=0
for x in range(n):
    s=s*10+2
    c=c+s
print(c)





'''
Q.37 Write a program that prompts user to enter numbers.
The process repeats until the user enters -1.
Finally the program prints the count of prime and composite numbers entered.
'''

d=0
e=0
while True:
    a=int(input('Enter number:'))
    if a!=-1:
        c=0
        for i in range(1,a+1):
            if a%i==0:
                c+=1
        if c==2:
            d+=1
        elif c>2:
            e+=1
    else:
        print('The no. of prime numbers is:',d)
        print('The no. of composite numbers is:',e)
        break





#Q.38 Write a python program to operate like a calculator.

print('****Welcome to your Calculator application****')
a=float(input('Enter first number:'))
b=float(input('Enter second number:'))
s=a+b
d=a-b
p=a*b
q=a/b
f=a//b
r=a%b
e=a**b
def calc():
    print('''Enter operation you want to perform:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Floor Division
        6. Remainder
        7. Exponent''')
    n=int(input('Enter your choice:'))
    if n==1:
        print(s)
    elif n==2:
        print(d)
    elif n==3:
        print(p)
    elif n==4:
        print(q)
    elif n==5:
        print(f)
    elif n==6:
        print(r)
    elif n==7:
        print(e)
    else:
        print('Invalid Operation')
calc()
while True:
    i=input('Do you want to perform any other operations? Enter (Y/y/N/n):')
    if i=='Y' or i=='y':
        calc()
    elif i=='N' or i=='n':
        print('****Have a nice day****')
        break
    else:
        print('Invalid Operation')
        break





#Q.39 To implement remove() function of list

l=eval(input('Enter list with square brackets:'))
m=[]
a=eval(input('Enter element to remove:'))
for i in l:
    if i==a:
        a=None
    else:
        m.append(i)
print(m)





'''
Q.40 Given a list of numbers, find and print the first adjacent elements 
which have the same sign.
If there is no such pair, leave the output blank.
'''

l=[1,2,-2,5,6,-5,-9,3,6]
for i in range(len(l)-1):
    if (l[i]>0 and l[i+1]>0) or (l[i]<0 and l[i+1]<0):
        print([l[i],l[i+1]])





'''
Q.41 Given a list of numbers, determine and print the quantity of elements 
that are greater than both of their neighbours. The first and last items of
the list shouldn't be considered because they don't have two neighbours.
'''

c=0
l=[1,4,5,3,7,2,0,8]
for i in range(1,len(l)-1):
    if (l[i]>l[i+1]) and l[i]>l[i-1]:
        c+=1
        print(l[i])
print('The no. of elements greater than neighbours is:',c)





'''
Q.42 Given a list of numbers with all of its elements sorted in ascending
order, determine and print the quantity of distinct elements in it.
'''

l=[2,3,4,1,1,3,2,5,7,8,5,3]
l.sort()
print(l)
c=0
for i in l:
    if l.count(i)==1:
        c+=1
print('No. of distinct elements in the given list are:',c)





'''
Q.43 Given a list of unique numbers, swap the minimal and
maximal elements of this list, and print the resulting list.
'''

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





'''
Q.44 Given a list of numbers, find and print the elements 
that appear in the list only once. The elements must be printed in the order
in which they occur in the original list.
'''

l=[1,2,3,4,5,0,8,3,2,2,1,5,4]
m=[]
for i in l:
    if l.count(i)==1:
        m.append(i)
print(m)





'''
Q.45 Given a list of numbers, calculate and print the sum of numbers
which are at equal distance from both the ends.
'''

l=[1,2,3,4,5,6,7,8,9,10]
i=0
n=len(l)-1
while i<(len(l)/2):
    sum=l[i]+l[n]
    print(sum)
    i+=1
    n-=1           





'''
Q.46 Given a list of numbers, find and print all the
duplicate elements along with their index in the list.
'''

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





'''
Q.47 Write a python function to find max of 3 numbers
(by passing only two parameters).
'''

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(f'The maximum of given three numbers is:{max(c,max(a,b))}')





#Q.48 Write a python function to sum all the numbers in a list.
def listsum(l):
    s=0
    for i in l:
        s=s+i
    print('Sum is:',s)
l=eval(input('Enter list of numbers:'))
listsum(l)





'''
Q.49 Write a python function that takes a list and 
returns a list with distinct elements from the 1st list.
'''

l=eval(input('Enter list of numbers:'))
def func(l):
    m=[]
    for i in l:
        if l.count(i)==1:
            m.append(i)
    print(m)
func(l)





#Q.50 Write a python function to check whether a number is a perfect number or not.

n=int(input('Enter number to check for perfect number:'))
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if n==s:
        print('Perfect Number')
perfect(n)





#Q.51 Write a python function to implement Grading System.

n=int(input('Enter number of subjects for exam:'))
def grade(n):
    l=[]
    print(f'***Enter marks for student {j+1} in each subject***')
    for x in range(n):
        a=int(input('Enter marks:'))
        l.append(a)
    s=0
    for i in l:
        s=s+i
    avg=s/n
    print(f'Average marks of student {j+1} are {avg}')
    if avg>80:
        print('Grade=Excellent')
    elif avg>70 and avg<=80:
        print('Grade=A')
    elif avg>60 and avg<=70:
        print('Grade=B')
    elif avg>50 and avg<=60:
        print('Grade=C')
    elif avg>40 and avg<=50:
        print('Grade=D')
    elif avg>=35 and avg<=40:
        print('Grade=P')
    else:
        print('Grade=F (failed the exam)')
p=int(input('Enter number of students:'))
for j in range(p):
    grade(n)





#Q.52 Write a python function using recursion to find nth number in Fibonacci series.

def fibo(n):
    if n<0:
        print('Invalid no. of terms')
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input('Enter no. of terms:'))
for i in range(n):
    print(fibo(i))
print(f'{n}th term of Fibonaaci Series:',fibo(n-1))





#Q.53 Write a python function using recursion to find Factorial of a number.

def fact(n):
    if n<0:
        print('Factorial not possible..')
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input('Enter number for factorial:'))
print('Factorial is:',fact(n))





'''
Q.54 A cashier has currency notes of denominations 10, 50 and 100.
If the amount to be withdrawn is input through the keyboard in hundreds,
write a Python program using functions and find the total number of currency notes
of each denomination the cashier will have to give to the withdrawer.
'''

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





'''
Q.55 A library charges a fine for every book returned late. 
For first five days the fine is 50 paise, for 6 to 10 days fine is one rupee,
and above 10 days fine is five rupees.
If you return the book after 30 days your membership will be cancelled.
Write a Python program using functions to accept the number of days 
the member is late to return the book and display the fine or the appropriate message.
'''

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





'''
Q.56 Write a function called is_sorted() that is given a list and 
returns True if the list is sorted and False otherwise.
'''
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





'''
Q.57 Write a function called first_diff() that is given two strings and 
returns the first location in which the strings differ.
If the strings are identical, it should return -1.
'''

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





'''
Q.58 Write a function called thrice() that takes a list as an input and 
returns the numbers if there are multiples of the numbers present in the same list.
'''

l=eval(input('Enter a list of distinct numbers:'))
l.sort()
m=[]
def thrice(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)-1):
            if l[j]%l[i]==0 and i!=j:
                if l[i] not in m:
                    m.append(l[i])
    return m
print('The numbers which have their multiples in same list are:',thrice(l))





#Q.59 Write a python program to find out no. of occurrences of the maximum element in a list.

l=eval(input('Enter a list of numbers:'))
max=l[0]
c=0
for i in l:
    if i>max:
        max=i
for i in l:
    if l[i]==max:
        c+=1
print(f'Maximum number in list: {max},Occurence:{c}')





#Q.60 Write a python program to count the no. of vowels in a string

a='aeiouAEIOU'
b=input('Enter string:')
c=0
for i in b:
    if i in a:
        c+=1
print('No. of vowels:',c)





#Q.61 Write a python program to count the no. of consonants in a string.

a='aeiouAEIOU'
b=input('Enter string:')
c=0
for i in b:
    if i not in a and i.isalpha()==True :
        c+=1
print('No. of consonants:',c)





#Q.62 Write a python program to count the no. of occurrences of a word in a sentence.

a=input('Enter a sentence:')
b=input('Enter word you want to find:')
c=a.split()
d=0
for i in c:
    if b==i:
        d+=1
print('Word count:',d)





#Q.63 Write a python program to remove numbers from a given string.

a=input('Enter string:')
b=''
for i in a:
    if i.isdigit()!=True:
        b+=i
print(b)





#Q.64 Write a python program to check whether given string is a palindrome or not.

a=input('Enter string:')
b=a[::-1]
if a==b:
    print(a,'is palindrome')
else:
    print(a,'is not palindrome')





#Q.65 To check if substring is present in a string or not

a=input('Enter string:')
b=input('Enter string to search:')
if b in a:
    print(f'{b} is a substring present in {a}')
else:
    print(f'{b} is not a substring present in {a}')





#Q.66 To implement Binary Search

def search(l,x):            
    beg=0
    end=len(l)-1
    while beg<=end:
        mid=(beg+end)//2
        if x>l[mid]:
            beg=mid+1
        elif x<l[mid]:
            end=mid-1
        else:
            return mid
    return -1
l=eval(input('Enter list:'))
x=int(input('Enter number to search:'))
index=search(l,x)
if index!=-1:
    print('Element Index:',index)
else:
    print('Element not found in list..')





#Q.67 To implement Binary Search using recursion

def search(beg,end,l,x):        
    if beg>end:
        return -1
    mid=(beg+end)//2
    if x==l[mid]:
        return mid
    elif x>l[mid]:
        beg=mid+1
        return search(beg,end,l,x)
    else:
        end=mid-1
        return search(beg,end,l,x)
l=eval(input('Enter a sorted list:'))
x=int(input('Enter element to search:'))
index=search(0,len(l)-1,l,x)
if index==-1:
    print('Element not found in list')
else:
    print('Element Index:',index)





#Q.68 To implement Bubble Sort

l=eval(input('Enter a list of numbers:'))
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:                   
            l[j],l[j+1]=l[j+1],l[j]
print(l)





#Q.69 To implement Selection Sort

l=eval(input('Enter a list of numbers:'))
n=len(l)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
print('Sorted List:',l)





#Q.70 To implement Insertion Sort

l=eval(input('Enter a list of numbers:'))
for i in range(1,len(l)):
    k=l[i]
    j=i-1
    while j>=0 and k<l[j]:
        l[j+1]=l[j]
        j-=1
    else:
        l[j+1]=k
print(l)





'''
Q.71 Write a python program that takes input a text file and 
returns the no. of lines started with vowels.
'''

l='AEIOUaeiou'
f=open('file.txt')
s=f.readline()
c=0
while s:
    if s[0] in l:
        c+=1
    s=f.readline()
print('No. of lines starting with vowel:',c)





'''
Q.72 Write a python program that takes input a text file and 
returns the no. of lines started with consonants.
'''

l='AEIOUaeiou'
f=open('file.txt')
s=f.readline()
c=0
while s:
    if s[0] not in l and s[0].isalpha()==True:
        c+=1
    s=f.readline()
print('No. of lines starting with consonants:',c)





#Q.73 Write a python program to write numbers from 1 to 100 to a text file “numbers.txt”.

f=open('number.txt','w')
for i in range(1,101):
    f.write(str(i)+'\n')
f.close()





'''
Q.74  Write a python program to read a text file “story.txt” and 
return the number of lines starting with the word ‘This’.
'''

f=open('story.txt','r')
s=f.readline()
d=0
while s:
    l=s.split()
    if l[0]=='This':
        d+=1
    s=f.readline()
print("Lines starting with 'This':",d)





'''
Q.75 Write a python program to read a text file “story.txt” and
return the number of lines starting with the word ‘The’.
'''

f=open('story.txt','r')
s=f.readline()
d=0
while s:
    l=s.split()
    if l[0]=='The':
        d+=1
    s=f.readline()
print("Lines starting with 'The':",d)





'''
Q.76 Write a python program to reads a text file “story.txt” and
return the number of times the word “and” is present.
'''

f=open('file.txt','r')
s=f.read()
l=s.split()
p=0
for i in l:
    if i=='and':
        p+=1
print("Occurences of 'and':",p)
f.close()





#Q.77 Construct a triangle using turtle.

import turtle as t
a=t.Turtle()
for i in range(3):
    a.forward(100)
    a.left(120)
t.done()





#Q.78 Construct a square using turtle.

import turtle as t
a=t.Turtle()
for i in range(4):
    a.forward(100)
    a.left(90)
t.done()





#Q.79 Construct a rectangle using turtle.

import turtle as t
a=t.Turtle()
for i in range(2):
    a.forward(100)
    a.left(90)
    a.forward(50)
    a.left(90)
t.done()
