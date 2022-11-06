#Q2 pg no.265
print(6 == input("Value 1:"))
print(6 == int(input("value 2:")))
#Q4 (a)
a = va = 3
b = va = 3
print(a,b)
#(b)
a = 3
b = 3.0
print(a == b)
print(a is b)
#Q5 (a)
a,b,c = 1,1,2
d = a+b
e = 1.0
f = 1.0
g = 2.0
h = e+f
print(c == d)
print(c is d )
print(g == h)
print(g is h)
#Q5(b)
a = 5 - 4 - 3
b = 3**2**3
print(a)
print(b)
#Q5 (c)
a,b,c = 1,1,1
d = 0.3
e = a + b + c - d
f = a + b + c ==d
print(e)
print(f)
#Q6(a)
a = 12
b = 7.4
c = 1
a -= b
print(a,b)
a *= 2 + c
print(a)
b += a * c
print(b)
#Q6 (b)
x, y = 4, 8
z = x/y*y
print(z)
#Q15
a, b = bool(0), bool(0.0)
c, d = str(0), str(0.0)
#print(len(a), len(b))
print(len(c), len(d))
#Q17
a = True
b = 0 < 5
print(a == b)
print(a is b)
c = str(a)
d = str(b)
print(c == d)
print(c is d)
e = input("Enter :")
print(c == e)
print(c is e)
#Q19 (a)
x, y, z = True, False, False
a = x or (y and z)
b = (x or y) and z
print(a, b)
# (c)
s = 'Sipo'
s1 = s + '2'
s2 = s * 2
print(s1)
print(s2)
#(d)
w,x, y, z = True , 4, -6, 2
result = -(x + z) < y or x ** z <10
print(result)