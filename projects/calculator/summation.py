class calcValues:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

    def add(self):
        return self.x + self.y
    
    def subtract(self): 
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        return self.x / self.y
    
    def modulus(self):
        return self.x % self.y
    
    def exponent(self):                
        return self.x ** self.y
    
x = input('Enter first number: ')
y= input('Enter second number: ')
    
calculator = calcValues(x,y)

print(calculator)
print(f'The sum of {x} and {y} is {calculator.add()}')
print(f'The difference between {x} and {y} is {calculator.subtract()}')
print(f'The product of {x} and {y} is {calculator.multiply()}')
print(f'The division of {x} and {y} is {calculator.divide()}')
print(f'The modulus of {x} and {y} is {calculator.modulus()}')
print(f'The exponent of {x} and {y} is {calculator.exponent()}')