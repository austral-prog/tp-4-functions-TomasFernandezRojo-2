# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante == 0:
        r = -b / (2*a)
        return f"({r})"
    elif discriminante > 0:
        r1 = (-b - (discriminante**0.5)) / (2*a)
        r2 = (-b + (discriminante**0.5)) / (2*a)
        return f"({r2}, {r1})"
    else:
        return "( )"
    
    
    
    
        

def value_y(a, b, c, x):
    cuadratica = a*x**2 + b*x +c 
    return cuadratica


def to_string(a, b, c):
    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return f"f(x) = {c}"


def derivation(a, b, c):
    if a != 0 and b != 0:
        return f"f'(x) = {a * 2} * X + {b}"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    elif a != 0 and b == 0:
        return f"f'(x) = {a * 2} * X"
    else:
        return f"f'(x) = 0"
    
    
print(roots(1, -3, 2))
print(value_y(1, -3, 2, 0))
print(to_string(2, -3, 1))
print(derivation(2, -3, 1))