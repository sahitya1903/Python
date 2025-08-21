a=int(input('Enter the end value till which you want to find the sum of cubes:'))
s=0
for x in range(0,a+1):
    s=s+x**3
print('The sum of cubes upto end value is:',s)
d=(a**4+2*a**3+a**2)/4
if s==d:
    print('The values are checked and verified as correct.')

a=int(input('Enter the end value till which you want sum of squares:'))
s=0
for x in range(0,a+1):
    s=s+pow(x,2)
print('The sum of squares upto end value is:',s)
d=(2*pow(a,3)+3*pow(a,2)+a)/6
if s==d:
    print('The values are checked and verified as correct.')

a=int(input('Enter the number till which you want to calculate the sum:'))
s=0
for x in range(a+1):
    s=s+x
print('The sum is:',s)
d=(a**2+a)/2
if s==d:
    print('The values are checked and verified as correct.')

n=int(input('Enter number of terms in series:'))
s=0
c=0
for x in range(n):
    s=s*10+2
    c=c+s
print(c)