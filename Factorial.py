#find the factorial of given number
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of given number is",fact)

####################################################
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
#####################################################
#we can find a factorial by using recursion 
def rfact(n):
    print(__name__)
    if n==0:
        return 1
    return n*fact(n-1)

def main():
    n = int(input("Enter a number:"))
    result = fact(n)
    print(result)
    print("---------------------------------")
    n = int(input("Enter a number:"))
    result = rfact(n)
    print(result)

if (__name__)=="__main__":
    main()