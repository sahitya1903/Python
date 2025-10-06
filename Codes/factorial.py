# a=int(input('Enter a number for factorial:'))
# p=1
# while a>0:
#     p=p*a
#     a=a-1
# print(p)
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
