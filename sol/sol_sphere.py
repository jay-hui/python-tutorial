# given the radius, r, as an input, print out the volume of the sphere.
# for your convenience, the formula for the volume of a sphere:
# V = (4/3) * pi * r^3
# sample input:         sample output:
# 6                     904.7786842338603

pi = 3.1415926535897931 # the constant pi is given

### SOLUTION BELOW ###

r = int(input())
V = 4.0/3.0 * pi * r**3
print(V)