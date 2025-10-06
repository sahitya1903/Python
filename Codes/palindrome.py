a=input('Enter number to check for palindrome:')
b=(len(a)-1)
c=0
for i in range(b):
    if a[i]==a[b-i]:
        c+=1
if c==b:
    print('Palindrome')

a=int(input('Enter number to check for palindrome:'))
n=a
s=0
while a>0:
    c=a%10
    s=s*10+c
    a=a//10
if n==s:
    print('Palindrome')