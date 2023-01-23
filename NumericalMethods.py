def bisection(f, a, b, tol=1e-5):
  """Find root of f(x) = 0 on interval [a,b] to within tolerance tol using bisection method"""
  if f(a)*f(b) > 0:
    raise ValueError("f(a) and f(b) must have opposite signs")
  while b - a > tol:
    c = (a + b)/2
    if f(c) == 0:
      return c
    elif f(a)*f(c) < 0:
      b = c
    else:
      a = c
  return (a + b)/2

def false_position(f, a, b, tol=1e-5):
  """Find root of f(x) = 0 on interval [a,b] to within tolerance tol using regular falsi method"""
  if f(a)*f(b) > 0:
    raise ValueError("f(a) and f(b) must have opposite signs")
  while b - a > tol:
    c = (a*f(b) - b*f(a))/(f(b) - f(a))
    if f(c) == 0:
      return c
    elif f(a)*f(c) < 0:
      b = c
    else:
      a = c
  return (a + b)/2

def newton_raphson(f, df, x0, tol=1e-5):
  """Find root of f(x) = 0 using Newton-Raphson method with initial guess x0"""
  x = x0
  while abs(f(x)) > tol:
    x = x - f(x)/df(x)
  return x