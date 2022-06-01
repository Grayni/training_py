from scipy.optimize import golden as gl
from two_functions import f, g

# find min value of function

print(f(gl(f, brack=(-10, -4))))
print(g(gl(g, brack=(-10, -4))))


#print(gl(f, brack=(-10, -4)))
#print(gl(g, brack=(-10, -4)))

