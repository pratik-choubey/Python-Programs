#1

#1
#23
#456
#78910
N = int(input("Enter no of rows:"))
start = 1
for i in range(1,N+1):
    for j in range(i):
        print("",start,end="")
        start+=1
    print()
#2
#1
#11
#111
#1111
#11111
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    for j in range(i):
        print("1",end="")
    print()

#3
#1
#22
#333
#4444
#55555
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    for j in range(i):
        print(i,end="")
    print()
#4
# 1
# 12
# 123
# 1234
# 12345
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
#5
#    1
#   1 1
#  1 1 1
# 1 1 1 1 
#1 1 1 1 1 
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(i):
        print("","1",end="")
    print()
#6
#       1
#      1 2
#     1 2 3
#    1 2 3 4
#   1 2 3 4 5 
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("",j,end="")
    print()
#7
#       1
#      2 3
#     4 5 6
#    7 8 9 10
N = int(input("Enter no of rows:"))
start = 1
for i in range(1,N+1):
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(i):
        print("",start,end="")
        start+=1
    print()
#8
#    1
#   2 2
#  3 3 3 
# 4 4 4 4  
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(i):
        print("",i,end="")
    print()

#9
#54321
#4321
#321
#21
#1
N = int(input("Enter no of rows:"))
for i in range(N,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()