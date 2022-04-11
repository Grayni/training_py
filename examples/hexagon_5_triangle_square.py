# hexagon + 5 triangle square
side = 85

# formula: 11 * S_triangle
# S_triangle = (p * (p - side)**3)**0.5
# p = 1.5 * side

p = 1.5 * side
s_triangle = (p * (p - side)**3)**0.5
S = 11 * s_triangle
print(round(S))
