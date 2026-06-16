a='aeiouAEIOU'
b=input('Enter string:')
c=0
for i in b:
    if i in a:
        c+=1
print('No. of vowels:',c)

a='aeiouAEIOU'
b=input('Enter string:')
c=0
for i in b:
    if i not in a and i.isalpha()==True :
        c+=1
print('No. of consonants:',c)

a=input('Enter string:')
b=''
for i in a:
    if i.isdigit()!=True:
        b+=i
print(b)

a=input('Enter a sentence:')
b=input('Enter word you want to find:')
c=a.split()
d=0
for i in c:
    if b==i:
        d+=1
print('Word count:',d)

a=input('Enter string:')
b=a[::-1]
if a==b:
    print(a,'is palindrome')
else:
    print(a,'is not palindrome')

a=input('Enter string:')
b=input('Enter string to search:')
if b in a:
    print(f'{b} is a substring present in {a}')
else:
    print(f'{b} is not a substring present in {a}')

a=input('Enter first string:')
b=input('Enter second string:')
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            print('Strings not equivalent')
            break
    print('Strings equivalent')
else:
    print('Strings not equivalent')
