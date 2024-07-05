#Fibonacci series by using simple method
n = int(input("Enter No. of terms:"))
first = 0
second = 1
print(first)
print(second)
for _ in range(n-2):
    next = first + second
    print(next)
    first = second
    second = next

#fibonacci series by using recursion
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


    