class Calculator:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):
        return self.__a + self.__b

    def subtract(self):
        return self.__a - self.__b

    def set_values(self, a, b):
        self.__a = a
        self.__b = b

    def get_values(self):
        return (self.__a, self.__b)

calculator = Calculator(10, 5)

print("Addition:", calculator.add())  

print("Subtraction:", calculator.subtract())  

calculator.set_values(20, 8)

print("Addition with new values:", calculator.add()) 

print("Subtraction with new values:", calculator.subtract())  

print("Current values:", calculator.get_values())  
