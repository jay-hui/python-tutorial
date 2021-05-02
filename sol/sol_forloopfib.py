# print out the n-th number of the fibonacci sequence.
# fibonacci sequence: 1, 1, 2, 3, 5, 8, ...
# sample input:         sample output:
# 5                     5
# sample input:         sample output:
# 19                    4181

### SOLUTION BELOW ###

n = int(input())
number1, number2 = 1, 1
for i in range(3, n+1):
    number2 += number1 # number2 = number2 + number1
    number1, number2 = number2, number1
print(number1)