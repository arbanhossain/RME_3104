from FindRoot import *

precision_digits = 4
tolerance = 10**(-precision_digits)

f = lambda x: x**2 - 2

print(f"Following results are {precision_digits} digits accurate")
print(f"Bisection method: {bisection(f, 1, 5, tolerance)}")
print(f"False Position method: {false_position(f, 0.5, 4, tolerance)}")
print(f"Newton Raphson method: {newton_raphson(f, lambda x: 2*x, 3, tolerance)}")