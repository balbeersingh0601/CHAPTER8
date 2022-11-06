#Q23
'''P = float(input("Enter Principle amount"))
R = float(input("Enter rate of interest"))
t = float(input("Enter number of years"))
si = ((P*R*t)/100)
print("Simple interest is", si)
print("Amount Payable is",P+si)
'''
#Q24
import math
P = float(input("Enter Principle amount"))
R = float(input("Enter rate of interest"))
t = float(input("Enter number of years"))
d = ( 1+(R/100))
l = math.pow(d,t)
A = P*l
ci = A + P
print("Compound interest is", A)
print("Amount payable is", ci)