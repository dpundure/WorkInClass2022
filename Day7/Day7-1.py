def add_mult(a, b, c):
    a, b, c = sorted([a, b, c])
    print(f"equation: ({a} + {b}) * {c}")
    return (a + b) * c

result = add_mult(1, 4, 21)
print(result)