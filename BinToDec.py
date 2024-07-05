n = int(input("Enter binary number(in 0 and 1 form):"))
n = str(n)[::-1]
l = len(n)
decimal = 0
for i in range(0, l):
    decimal = decimal + int(n[i])*(2**i)
print(decimal)
