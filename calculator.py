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
    def Method1(self , operator):
        if(operator == '+'):  
            return Div.additon()
        elif(operator == '-'):
            return Div.substraction()
        elif(operator == '*'):
            return Div.multiplication()
        elif(operator == '/'):
            return Div.division()
        else:
           return print("entered operator is invalid")

a = int(input('enter the first number : '))
while True:
    operator = (input('Please enter operator : ')) 
    if(operator == '='):
        print("resultant ",calculatedvalue)
        break
    else:
        b = int(input('enter the second number : '))    
        Div = Calculator(a,b)
        calculatedvalue =  Div.Method1(operator)
        a = calculatedvalue
        print("now a became" , a)






