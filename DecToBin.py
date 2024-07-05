# n = int(input("Enter a decimal number:"))
# binary = ""
# while n>0:
#     rem = n%2
#     binary = binary + str(rem)
#     n=n//2
# print("0b"+binary[::-1])
# #built in function
# print(bin(12))


n = int(input())
binary = ""
count = 0
while n > 0:
    rem = n % 2
    if int(rem) == 1:
        count = count+1
    n = n//2
print(count)
