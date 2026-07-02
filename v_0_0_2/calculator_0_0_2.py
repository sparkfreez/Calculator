class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Can not divide by zero"
        return a / b

#create Object
cal = Calculator()

print("++++----****////")
print("Simple Calulator")
print("++++----****////")

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter only integers or decimal numbers.")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose Operation (1-4): ")

if choice == "1":
    print("Resulte: ", cal.add(a, b))

elif choice == "2":
    print("Resulte: ", cal.sub(a, b))

elif choice == "3":
    print("Resulte: ", cal.multiply(a, b))

elif choice == "4":
    print("Resulte: ", cal.divide(a, b))

else:
    print("Invalid choice")
