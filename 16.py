import random
import statistics # u can use different function of random module
r1 = random.random()
r2 = random.random()
r3 = random.random()
r4 = random.randrange(10) # range defined
r5 = random.randrange(10, 16)# with start & stop
r6 = random.randrange(10, 16,2)# with start & stop & step
seq = [r1,r2,r3,r4,r5,r6]
print(seq)
print("Mean of the sequence",statistics.mean(seq))
print("Median of the sequence",statistics.median(seq))
print("Mode of the sequence",statistics.mode(seq))