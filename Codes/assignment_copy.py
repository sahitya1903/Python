# n=int(input('Enter number for table upto 20 steps:'))
# for i in range(1,21):
#     if i==n:
#         print(f'* x * = {n*i}')
#     else:
#         print(f'{n} X {i} = {n*i}')

l=[]
for i in range(1,101):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        l.append(str(i))
m=[]
for k in l:
    if k[::-1] in l:
        m.append(int(k))
print(f'List of prime numbers upto 100 having their reverse as prime:\n{m}')