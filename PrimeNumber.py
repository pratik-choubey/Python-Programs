#find given nuber is a prime or not 
n = int(input("Enter a number:"))
if n==0:
    print("Given no. is not a prime")
elif n==1:
    print("Given no is not a prime")
else:
    for i in range(2,n//2):
        if n%i==0:
            print("Given no. is not a prime")
            break
    else:
        print("Given no is prime")