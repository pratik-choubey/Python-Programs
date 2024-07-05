#1st method 
a=9
b=8
print("Before swaping:",a,b)
a,b=b,a
print("after swaping",a,b)
#2nd method without third variable
a=12
b=13
print("Before swaping:",a,b)
a=a+b
b=a-b
a=a-b
print("after swaping",a,b)
#3rd method without third variable
a=15
b=16
print("Before swaping:",a,b)
a=a*b
b=a//b
a=a//b
print("after swaping",a,b)
#4th method by using third variable
a=10
b=20
print("Before swaping:",a,b)
c=a
a=b
b=c
print("after swaping",a,b)

