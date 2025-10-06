# l=[2,4,6,5,3,2,1,4,5,6,8,9,8,7,6,9,9,9,4,3,2]
# m=[]
# n=[]
# max=max(l)
# min=min(l)
# c=0
# for i in l:
#     if i==max:
#         m.append(c)
#     elif i==min:
#         n.append(c)
#     c+=1
# print(m)
# print(n)


# def rotate_list(lst, k):
#     k %= len(lst)  # Handle rotations greater than list length
#     return lst[-k:] + lst[:-k]

# lst = [1, 2, 3, 4, 5]
# rotated = rotate_list(lst, 2)  # Rotate right by 2
# print(rotated)  # Output: [4, 5, 1, 2, 3]

# import random

# def select_EC253HW2problems():

#     problem_nos = list(range(1, 51))
   
#     user_input = int(input("Enter the last two digits of your Roll Number"))
               
#     # Give seed such that same result is obtained every time for given roll no
#     random.seed(user_input)
   
#     # Select 8 random problems
#     selected_problems = sorted(random.sample(problem_nos, 8))

#     return selected_problems

# selected_problems = select_EC253HW2problems()    
# print("Your 8 selected problems are:", selected_problems)
# print("Please Submit the solution of these problems before the deadline")


import numpy as np

# Define the input signal
x = [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]

# Compute the FFT
fft_result = np.fft.fft(x)

# Get magnitude spectrum
magnitude = np.abs(fft_result)

# Round for easier reading
rounded_magnitude = np.round(magnitude, 2)

print(rounded_magnitude)
