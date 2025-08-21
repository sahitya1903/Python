m=['!','@','#','$','%','^','&','*','_','-','+','=',':',';','.','/','<','>',',','?']
while True:
    print('''While entering a password, remember 3 conditions:
1. It must contain a lower case and an upper case letter.
2. It must contain a special symbol. [ ! @ # $ % ^ & * _ - + = : ; , . / < > ? ]
3. It must contain a minimum of 8 characters and not more than 15 characters.''')
    a=input('Enter your Password to set:')
    c=0
    d=0
    e=0
    for i in a:
        if i.islower()==True:
            c+=1
        elif i.isupper()==True:
            d+=1
        elif i in m:
            e+=1
    if len(a)>=8 and len(a)<=15 and (c+d+e)>=3:
        c=input('Confirm password:')
        print('Password set successfully..')
        break
    else:
        print('Invalid Password. Enter a new password again.')