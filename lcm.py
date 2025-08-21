c=0
while True:
    c+=10
    s=0
    for x in range(1,11):
        if c%x==0:
            s+=1
    if s==10:
        print(c)
        break
    else:
        continue