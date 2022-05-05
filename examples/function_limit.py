def limit_func(x):
    return (2*x**2-3*x-5) / (3*x**2+x+1)

print(round(limit_func(1e6), 3))
print(round(limit_func(-1e26), 3))
