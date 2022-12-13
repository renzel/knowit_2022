# Import math Library
import math

h = 160
r = 50
height = math.sqrt(r**2 + h**2)
areal = (math.pi * r * height) / 100


kuler = [(4,10), (4,15), (2,30), (5,15)]
kostnad = 0
for kule in kuler:
    kostnad += areal / 100 * kule[0] * kule[1]

print(round(kostnad, -1))