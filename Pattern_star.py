#Pattern * 
#1st pattern
# *   
# **  
# *** 
# ****
# *****
# ******
r = int(input("Enter number of rows:"))
for i in range(r+1):
    for j in range(i+1):
        print("*",end="")
    print()
#2nd pattern
#         *
#        * *
#       * * *
#      * * * *
#     * * * * *
for i in range(r+1):
    for space in range(r-i+1):
        print(" ", end="")
    for j in range(i+1):
        print("* ",end="")
    print()
#3rd pattern
#       *
#      **
#     ***
#    ****
#   *****
#  ******
for i in range(r+1):
    for space in range(r-i+1):
        print(" ", end="")
    for j in range(i+1):
        print("*",end="")
    print()
