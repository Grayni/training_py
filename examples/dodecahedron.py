# S and V dodecahedron
side = 1

S = 3 * side**2 * (5 * (5 + 2 * 5**0.5))**0.5
V = (side**3) / 4 * (15 + 7 * 5**0.5)
print(round(S, 2))
print(round(V, 2))
