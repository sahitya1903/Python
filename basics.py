for x in range(1,13,2):
    print(x)

a=int(input('Enter the starting value from which descending order starts:'))
while a>0:
    print(a)
    a=a-1

for x in range(-10,-1):
    print(x)

# print('****Welcome to Book My Tickets App..****')
# a=int(input('Enter the number of Tickets you want to purchase:'))
# b=300
# tot=a*b
# print('Your total bill is',tot)
# p=input('Do you want to continue the purchase? (y/n)')
# if p=='y':
#     for x in range(a):
#         print('''The movies for today are:
# 1. Salaar                 9:00 am - 12:00 pm
# 2. 12th fail              12:30 pm - 3:30 pm
# 3. Leo                    4:00 pm  - 7:00 pm
# 4. Dhamaal                7:30 pm  - 9:30 pm''')
#         s=int(input('Select the movie you want to watch by entering its number:'))
#         name=input('Enter name of person:')
#         age=int(input('Enter age:'))
#         print('Details Entered successfully..')
#         print('Booking details are:', [name,age],' Your Movie Number is',s)
#     print('''Please reach at least 10 minutes prior to the movie timing in order to avoid rush..
# Thanks to consider Book My Ticket App as your Ticket Vendor..
# We are happy to serve you...''')
# elif p=='n':
#     print('See you on your next movie plan..')
# else:
#     print('Sorry.. Invalid Operation..')

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



a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
if a>b:
    print(a,'is greater')
elif a==b:
    print('Both a and b are equal to', a)
else:
    print(b,'is greater')

#Program to calculate greatest of three numbers
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
if (a>=b and a>=c):
    print(a,'is greatest')
elif (b>=a and b>=c):
    print(b,'is greatest')
else:
    print(c,'is greatest')

a=int(input('Enter the number whose table you want to print:'))
b=int(input('Enter the number of steps of the table:'))
for x in range(1,b+1):
    print(a,'*',x,'=',a*x)

#program for time table
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


print('****Welcome to Book My Tickets App..****')
a=int(input('Enter the number of Tickets you want to purchase:'))
b=300
tot=a*b
print('Your total bill is',tot)
age=int(input('enter age:'))
print('age is', age)


a=int(input('Enter starting value:'))
b=int(input('Enter end value:'))
for x in range(a,b+1):
    print(x)