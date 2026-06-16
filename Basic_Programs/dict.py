d={}
a=int(input('Enter number of students:'))
for i in range(a):
    r=input('Enter roll no.:')
    ph=int(input('Enter marks for PH:'))
    ch=int(input('Enter marks for CH:'))
    ma=int(input('Enter marks for MA:'))
    bg=int(input('Enter marks for BG:'))
    es=(ph+ch+ma)/3
    ms=(ph+ch+bg)/3
    s={r:{'PH':ph,'CH':ch,'MA':ma,'BG':bg,'ES-MS':(es,ms)}}
    d.update(s)
print(d)
