from scipy.optimize import golden as gl
from two_functions import f, g

print(gl(f))
print(gl(g))
