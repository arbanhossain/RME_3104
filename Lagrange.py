from itertools import zip_longest, product

class Polynomial:
  def __init__(self, coefficients):
    self.coefficients = coefficients

  def __call__(self, x):
    return sum(c * x**i for i, c in enumerate(self.coefficients))

  def __add__(self, other):
    if isinstance(other, Polynomial): return Polynomial([a + b for a, b in zip_longest(self.coefficients, other.coefficients, fillvalue=0)])

  def __sub__(self, other):
    return Polynomial([a - b for a, b in zip_longest(self.coefficients, other.coefficients, fillvalue=0)])

  def __truediv__(self, other):
    if isinstance(other, (int, float)): return Polynomial([c / other for c in self.coefficients])
    if isinstance(other, Polynomial): return Polynomial([sum(a / b for a, b in product(self.coefficients, other.coefficients))])
  
  def __mul__(self, other):
    if isinstance(other, (int, float)): return Polynomial([c * other for c in self.coefficients])
    res = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
    for i in range(len(self.coefficients)):
      for j in range(len(other.coefficients)):
        res[i + j] += self.coefficients[i] * other.coefficients[j]
    return Polynomial(res)

  def __str__(self):
    return " + ".join(f"{c}x^{i}" for i, c in enumerate(self.coefficients) if c != 0)

  def __repr__(self):
    return f"Polynomial({self.coefficients})"

  def __eq__(self, other):
    return self.coefficients == other.coefficients

  def __ne__(self, other):
    return self.coefficients != other.coefficients


def lagrange_interpolation(points):
  """Find the polynomial of least degree that passes through the given points"""
  n = len(points)
  x = [p[0] for p in points]
  y = [p[1] for p in points]
  L = [Polynomial([1])] * n
  for i in range(n):
    for j in range(n):
      if i != j:
        L[i] = L[i] * Polynomial([-x[j], 1]) / (x[i] - x[j])
  for i in range(n):
    L[i] = L[i] * y[i]
  x = Polynomial(L[0].coefficients)
  for i in range(1, n):
    x = x + L[i]
  return x

if __name__ == "__main__":
  # print(Polynomial([-2, 1]) * Polynomial([-3, 1]))
  pairs = [(1, 1), (2, 3), (3, 2)]
  F = lagrange_interpolation(pairs)

  print(pairs)
  print(F)
  print(" ".join(f"F({x})={F(x)}" for x, y in pairs))