class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

a = float(input('Enter First number : '))
b = float(input('Enter Second number : '))        
obj=calculator(a,b)
while True:
    def menu():
        x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide') 
        print(x)
    menu()
    choice = str(input('Please select one of the following : ')) 
    if choice == 'Add':
        print("Result: ",obj.add())
    elif choice == 'Sub':
        print("Result: ",obj.sub())
    elif choice == 'Multiply':
        print("Result: ",obj.multiply())    
    elif choice == 'Divide':
        print("Result: ",obj.divide())
    elif choice == 0:
        print('Try again')
        break
    else:
        print('Invalid option') 
        break       
print()
