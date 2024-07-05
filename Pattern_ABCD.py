#1
#A
#AB
#ABC
#ABCD
#ABCDE
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    start = ord("A")
    for j in range(i):
        print(chr(start),end="")
        start+=1
    print()
#2
#A
#AA
#AAA
#AAAA
#AAAAA
N = int(input("Enter no of rows:"))
start = ord("A")
for i in range(1,N+1):
    for j in range(i):
        print(chr(start),end="")
    print()

#3
#A
#BB
#CCC
#DDDD
#EEEEE
N = int(input("Enter no of rows:"))
start = ord("A")
for i in range(1,N+1):
    for j in range(i):
        print(chr(start),end="")
    start+=1
    print()
#4
# A
# BC
# DEF
# GHIJ
# KLMNO
N = int(input("Enter no of rows:"))
start = ord("A")
for i in range(1,N+1):
    for j in range(i):
        print(chr(start),end="")
        start+=1
    print()
####################################################################################
#5
#    A
#   A A
#  A A A
# A A A A 
#A A A A A 
N = int(input("Enter no of rows:"))
start = ord("A")
for i in range(1,N+1):
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(i):
        print("",chr(start),end="")
    print()
#6
#    A
#   A B
#  A B C
# A B C D  
#A B C D E 
N = int(input("Enter no of rows:"))
for i in range(1,N+1):
    start = ord("A")
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(i):
        print("",chr(start),end="")
        start+=1
    print()
#7
#       A   
#      B C  
#     D E F 
#    G H I J
#   K L M N O
N = int(input("Enter no of rows:"))
start = ord("A")
for i in range(1,N+1):
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(i):
        print("",chr(start),end="")
        start+=1
    print()
#8
#    A
#   B B
#  C C c
# D D D D 
N = int(input("Enter no of rows:"))
start = ord("A")
for i in range(1,N+1):
    for k in range(N-i+1):
        print(" ",end="")
    for j in range(i):
        print("",chr(start),end="")
    start+=1
    print()
#9
#ABCDE
#ABCD
#ABC
#AB
#A
N = int(input("Enter no of rows:"))
for i in range(N,0,-1):
    start=ord("A")
    for j in range(i,0,-1):
        print(chr(start),end="")
        start+=1
    print()

