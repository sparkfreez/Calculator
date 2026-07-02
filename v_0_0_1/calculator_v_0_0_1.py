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
calc = Calculator()

#use methods
print("Addition of 10 & 5 : ",calc.add(10, 5)) 

print("Substraction of 5 & 5 : ",calc.sub(5, 5))

print("Multiplicatiom of 999 & 99 : ",calc.multiply(999, 99))

print("Division of 27 & 9 : ",calc.divide(27, 9))
