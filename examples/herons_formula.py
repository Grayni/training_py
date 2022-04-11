# find S triangle on 3 sides

a = 5
b = 5
c = 5

# formula: S = sqrt(p(p-a)(p-b)(p-c))
# p = (a+b+c)/2

p = (a + b + c)/2
print((p * (p - a) * (p - b) * (p - c))**0.5)
