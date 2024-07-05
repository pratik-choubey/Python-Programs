def LcmIs( x , y ):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if(greater % x == 0 and greater % y == 0):
            LCM = greater
            break
        greater += 1
    return LCM
a = int(input("Enter first Number:"))
b = int(input("Enter second Number:"))
print(LcmIs( a, b))
