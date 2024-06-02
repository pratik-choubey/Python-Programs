#find the number is armstrong or not
'''An Amrstrong number is a number that is equal to the sum of 
its own digits each raised to the power of the number of digits.'''
n = int(input("Enter a number:"))
N=str(n)
sum = 0
for i in range(0,len(N)):
    sum = sum + int(N[i])**len(N)
if sum == n:
    print("Given number is a armstrong")
else:
    print("Given number is not a armstrong")




