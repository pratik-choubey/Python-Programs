#Pattern --> Pascal's triangle
#method-1 it is only aplicable upto 0 to 5
r = int(input("Enter no of rows:"))
for i in range(0,r+1):
    print(11**i)
#method-2
from math import factorial
# input n
n = 5
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    # for new line
    print()