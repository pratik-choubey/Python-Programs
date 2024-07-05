# GCD of two number:-(Greatest common divisor)
'''-->A simple solution is to find all prime factors of both numbers,
then find intersection of all factors present in both numbers. 
Finally return product of elements in the intersection.
-->An efficient solution is to use "Euclidean algorithm" which is the
main algorithm used for this purpose. The idea is, GCD of two numbers
doesn’t change if smaller number is subtracted from a bigger number.'''
a = int(input("Enter first Number:"))
b = int(input("Enter second Number:"))


def GcdIs(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return b
    if a > b:
        return GcdIs(a-b, a)
    return GcdIs(a, b-a)


if (GcdIs(a, b)):
    print("GCD of given number is:", GcdIs(a, b))
else:
    print("GCD Not Found")
# When we find the differnce of greater no to the next no. than no change in
# GCD if a>b then gcd of a and b is same gcd of a-b and b
