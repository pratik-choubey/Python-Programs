#Code-1 == Reverse a string 
s = input("Enter a string to get reverse string:")
#method 1
print(s[::-1])
#method 2
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')