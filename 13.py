import random
import statistics
r1 = random.randrange(10, 16, 1)
r2 = random.randrange(10, 16, 1)
r3 = random.randrange(10, 16, 1)
r4 = random.randrange(10, 16, 1)
r5 = random.randrange(10, 16, 1)
r6 = random.randrange(10, 16, 1)
seq = [r1,r2,r3,r4,r5,r6]
print(seq)
print("Mean of the sequence",statistics.mean(seq))
print("Median of the sequence",statistics.median(seq))
print("Mode of the sequence",statistics.mode(seq))