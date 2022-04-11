# Sum S hexagon and S 3 squares and 6 S triangles
# pic: ~/pictures/triangles_squares_hexagon.jpg
side = 8


def S_triangle(s):
    p = s * 1.5
    return (p * (p - s) ** 3) ** 0.5


s_small_triangle = S_triangle(side/2)
s_square = side**2

S = 3 * s_square + 30 * s_small_triangle
print(round(S))



