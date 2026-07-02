import math

class AdvanceCalculater:

  def add(self, a, b):
    return a + b

  def sub(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    if b == 0:
            return "Error: Division by zero"
    return a / b

  def power(self, a, b):
        return a ** b

  def square_root(self, a):
    return math.sqrt(a)

  def factorial(,self, n):
    return math.factorial(n)

  def sin(self, angle):
    return math.sin(math.radians(angle))

  def cos(self, angle):
    return math.cos(math.radians(angle))

  def tan(self, angle):
    return math.tan(math.radians(angle))

  def log(self, n):
    return math.log10(n)

  def ln(self, n):
    return math.log(n)

  def gcd(self, a, b):
    return math.gcd(a, b)

  def lcm(self, a, b):
    return abs(a * b) // math.gcd(a, b)

  def permutations(self, n, r):
    return math.perm(n, r)

  def combinations(self, n, r):
    return math.comb(n, r)