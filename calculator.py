class Calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def additon(self):
        return self.a + self.b
    def substraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b

a = int(input('enter the first number : '))
operator = (input('Please enter operator : ')) 
b = int(input('enter the second number : '))    

Div = Calculator(a,b)

if(operator == '+'):
    print("Resultant value:" ,Div.additon())
elif(operator == '-'):
    print("Resultant value:" ,Div.substraction())
elif(operator == '*'):
    print("Resultant value:" ,Div.multiplication())
elif(operator == '/'):
    print("Resultnt value:" ,Div.division())
else:
    print("entered operator is invalid")
    





