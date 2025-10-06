f=open('number.txt','w')
for i in range(1,101):
    f.write(str(i)+'\n')
f.close()
f=open('numbers.txt','r')
s=f.read()
print(s)
f.close()


# l='AEIOUaeiou'                            #using readlines()
# f=open('file.txt','w')
# for i in range(65,90):
#     f.write(chr(i)+chr(i+1)+'\n')
# f.close()
# f=open('file.txt','r')
# c=0
# s=f.readlines()
# for i in s:
#     if i[0] in l:
#         print(i)
#         c+=1
# print('No. of lines starting with vowels:',c)
# f.close()

l='AEIOUaeiou'                            #using readline()
f=open('file.txt')
s=f.readline()
c=0
while s:
    if s[0] in l:
        c+=1
    s=f.readline()
print('No. of lines starting with vowel:',c)


f=open('file.txt','r')
s=f.read()
l=s.split()
p=0
for i in l:
    if i=='and':
        p+=1
print("Occurences of 'and':",p)
f.close()

f=open('story.txt','r')
s=f.readline()
d=0
while s:
    l=s.split()
    if l[0]=='The':
        d+=1
    s=f.readline()
print("Lines starting with 'The':",d)
