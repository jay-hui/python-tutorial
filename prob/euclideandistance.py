# given 4 integer inputs, x1, y1, x2, y2, calculate the euclidean distance between (x1, y1) and (x2, y2).
# hint: pythagoras' theorem: c^2 = a^2 + b^2
# sqrt(4) = 2, sqrt(25) = 5
# sample input:         sample output:
# -2 -3 6 8             13.601470508735444

import math

### TYPE YOUR CODE BELOW ###

x1, y1, x2, y2 = list(map(int, input().split()))
a = x2-x1
b = y2-y1
print(math.sqrt(a**2+b**2))
