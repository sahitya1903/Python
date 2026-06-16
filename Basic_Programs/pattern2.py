r=int(input('Enter no. of rows:'))
for i in range(1,r+1):
    print('*'*i)


for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print('*',end='')
        else:
            print(' ',end='')
    print()
    

row=int(input('Enter no. of rows:'))
col=int(input('Enter no. of columns:'))
for i in range(1,row+1):
    for j in range(1,col+1):
        if i==j:
            print('*',end='')
        else:
            print(' ',end='')
    print()


r=int(input('Enter number of rows:'))
for i in range(1,r+1):
    print(' '*(r-i),end='')
    for j in range(1,i+1):
        print('* ',end='')
    print()

n=int(input('Enter no. of rows:'))
for k in range(1,n+1):
    print(' '*(n-k),end='')
    for l in range(1,k+1):
        print(l,'',end='')
    print()

