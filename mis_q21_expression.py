#Expression

import math
a=2
m=3
n=4
sum = m+n
c= math.pow(a,sum)
d= math.pow(a,m)*math.pow(a,n)
if (c==d):
    print("Expression worked")
else :
    print("Not worked")
'''
b = float(input("Enter the value"))   #(a)
h = float(input("Enter the value"))
print(1/3*math.pow(b,2)*h)
r = float(input("Enter the value"))   #(b)
print(math.pi*math.pow(r,2)*h)
print(1/3*math.pi*math.pow(r,2)*h)    #(c)
x1 = float(input("Enter the value")) #(d)
x2 = float(input("Enter the value"))
y1 = float(input("Enter the value"))
y2 = float(input("Enter the value"))
d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
print(d)'''
x = int(input("Enter the value of x"))
y = int(input("Enter the value of y"))
h = int(input("Enter the value of h"))
k = int(input("Enter the value of k"))
r =  (math.pow(x-h,2)+math.pow(y-k,2))
print("The value of expression (x-h)^2 + (y-k)^2 is ",math.pow(r,2))

