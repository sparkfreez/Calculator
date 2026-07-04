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

  def factorial(self, n):
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

calc = AdvanceCalculater()

while True:
    print("\n=== Advance Calculater ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("11. Log10")
    print("12. Natural Log")
    print("13. GCD")
    print("14. LCM")
    print("15. Permutation")
    print("16. Combination")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "0":
        break
      
    elif choice in ["1", "2", "3", "4","5","13","14"]:
        a = float(input("First number: "))
        b = float(input("Second number: "))

    if choice == "1":
        print(f"Result {a} + {b} = ", calc.add(a,b))
      
    if choice == "2":
        print(f"Result {a} - {b} = ", calc.sub(a,b))

    if choice == "3":
        print(f"Result {a} * {b} = ", calc.multiply(a,b))

    if choice == "4":
        print(f"Result {a} * {b} = ", calc.divide(a,b))

    if choice == "5":
        print(f"Result {a} * {b} = ", calc.power(a,b))

    if choice == "13":
        print(f"Result GCD of {a} and,{b} = ", calc.gcd(int(a), int(b)))

    if choice == "14":
        print(f"Result LCM of {a} and,{b} = ", calc.lcm(int(a), int(b)))

    if choice == "6":
        n = float(input("Number: "))
        print(f"Result sqrt of {n} = ", calc.square_root(int(n)))

    if choice == "7":
        n = float(input("Number: "))
        print(f"Result factorial of {n} = ", calc.factorial(int(n)))
              

    