import random
#Q14
print(random.randint(100,999)/5)
#Q15
print("Six Digit random OTP is", random.randint(100000,999999))
#12
a = random.randint(0, 5)
b = random.randint(0, 5)
print("Random numbers between 0 and 5 (A) :", a)
print("Random numbers between 0 and 5 (B)  :",b)
print("A to the power B =", a**b)
r = random.random() * 10
print(r, end = '')