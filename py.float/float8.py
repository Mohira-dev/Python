print("Float8")
import math
x = 0.4*pow(10, 4)
y = 0.5*math.sqrt(x)
print("Natija = " +str(pow((abs(math.cos(x)-math.cos(y))), (1+2*pow(math.sin(y), 2)))))