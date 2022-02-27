# import math module
import math

print(math.ceil(1.2))
print(math.fabs(-1.2))

# import specific function from module
from math import ceil, fsum, floor as myFloor

print(ceil(1.2))
print(fsum([1, 2]))
print(myFloor(1.9))

# imoprt my local module
from conditionals import plus
print(plus(10, 20))