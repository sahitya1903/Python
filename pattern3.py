n=int(input('Enter number of rows:'))       #Right angle triangle
for x in range(1,n+1):
    print('*'*x)

r=int(input('Enter number of rows:'))
for i in range(1,r+1):
    print(' '*(r-i)+i*'*')

n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

n=int(input('Enter number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i,0,-1):
        print(j,end='')
    print()

r=int(input('Enter no. of rows:'))
for i in range(r):
    for j in range(r-i,0,-1):
        print(j,end='')
    print()

n=int(input('Enter no. of rows:'))
for i in range(n):
    space= i%4
    if space == 3:
        space = 1
        for j in range (space):
            print(" ",end = "")
    else :
        for j in range(space):
            print(" ", end = "")
    print("*")