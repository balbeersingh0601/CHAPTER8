import math
a = int(input("Enter the value a "))
b = int(input("Enter the value b"))
print("The value of expression (a+b)^3 is ",math.pow(a,3)+ math.pow(b,3)+ 3*math.pow(a,2)*b+ 3*a*math.pow(b,2))
