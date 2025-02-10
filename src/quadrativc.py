import math
def find_roots(a, b, c):
    d = b**2 - 4*a*c  

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    elif d == 0:
        root = -b / (2*a)
        return root, root
    else:
        return None
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))

roots = find_roots(a, b, c)

if roots is None:
    print("No real roots.")
else:
    print("The roots are:", roots)
