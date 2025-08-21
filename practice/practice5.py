import random
import pyautogui as pg
import time
word=['Maddagudu','Eripuku','Koja','Lanja']
time.sleep(8)
for i in range(100):
    a=random.choice(word)
    pg.write(f'''You are {a}''')
    pg.press('enter')

# n=int(input('Enter number of lines:'))
# l=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(l,end=' ')
#         l+=1
#     print()


# n=int(input('Enter number of lines:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if (i+j)%2==0:
#             print(1,end='')
#         else:
#             print(0,end='')
#     print()


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,end='')
#     print(' '*2*(9-i),end='')
#     for k in range(i,0,-1):
#         print(k,end='')
#     print()
