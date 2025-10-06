l=eval(input('Enter a list of numbers:'))     #Bubble Sort
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:                   
            l[j],l[j+1]=l[j+1],l[j]
print(l)

l=eval(input('Enter a list of numbers:'))   #Selection Sort
n=len(l)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
print('Sorted List:',l)

l=eval(input('Enter a list of numbers:'))       #Insertion Sort
for i in range(1,len(l)):
    k=l[i]
    j=i-1
    while j>=0 and k<l[j]:
        l[j+1]=l[j]
        j-=1
    else:
        l[j+1]=k
print(l)

def search(l,x):            #Binary Search
    beg=0
    end=len(l)-1
    while beg<=end:
        mid=(beg+end)//2
        if x>l[mid]:
            beg=mid+1
        elif x<l[mid]:
            end=mid-1
        else:
            return mid
    return -1
l=eval(input('Enter list:'))
x=int(input('Enter number to search:'))
index=search(l,x)
if index!=-1:
    print('Element Index:',index)
else:
    print('Element not found in list..')

def search(beg,end,l,x):        #Binary Search using Recursion
    if beg>end:
        return -1
    mid=(beg+end)//2
    if x==l[mid]:
        return mid
    elif x>l[mid]:
        beg=mid+1
        return search(beg,end,l,x)
    else:
        end=mid-1
        return search(beg,end,l,x)
l=eval(input('Enter a sorted list:'))
x=int(input('Enter element to search:'))
index=search(0,len(l)-1,l,x)
if index==-1:
    print('Element not found in list')
else:
    print('Element Index:',index)

