# given 4 integer inputs, x1, y1, x2, y2, calculate the euclidean distance between (x1, y1) and (x2, y2).
# hint: pythagoras' theorem: c^2 = a^2 + b^2
# hint: please utilize the abs() function, and math.sqrt() function from the math library.
# abs(2) = 2, abs(-2) = 2
# sqrt(4) = 2, sqrt(25) = 5
# sample input:         sample output:
# -2 -3 6 8             13.601470508735444

import math

### SOLUTION BELOW ###

x1, y1, x2, y2 = list(map(int, input().split()))
d = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
print(d)