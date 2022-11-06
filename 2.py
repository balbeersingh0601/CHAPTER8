mon = float(input("Enter the temperature of Monday"))
tue = float(input("Enter the temperature of Tuesday"))
wed = float(input("Enter the temperature of Wednesday"))

thur = float(input("Enter the temperature of Thursday"))
fri = float(input("Enter the temperature of Friday"))
sat= float(input("Enter the temperature of Saturday"))
sun = float(input("Enter the temperature of Sunday"))

avg = int((mon + tue + wed + thur + fri + sat + sun)/7)
print(" The average temperature of the week ",avg)
