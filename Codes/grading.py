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