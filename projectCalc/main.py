#calculator

#add function
def add(num1, num2):  #function signature
    return num1 + num2

#sub function
def sub(num1, num2):
    return num1 - num2

#mult function
def mul(num1, num2):
    return num1 * num2

#div function
def div(num1, num2):
    return num1 / num2

#mod function
def mod(num1, num2):
    return num1 % num2

def main():
    operation = input("What do you want to do?(+, -, *, /, %) ")
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '%'):
        #invalid operation
        print ("You must enter a valid operation!")
    else:
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        if(operation == '+'):
            print(add(num1, num2))
        elif(operation == '-'):
            print(sub(num1,num2))
        elif(operation == '*'):
            print(mul(num1, num2))
        elif(operation == '/'):
            print(div(num1, num2))
        elif(operation == '%'):
            print(mod(num1, num2))
        else:
            print("Error")

main()
