def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    num1=float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    to_continue=True
    while to_continue:
        operation_symbol=input("Pick an operation: ")
        num2=float(input("Enter the next number: "))
        operation=operations[operation_symbol]
        answer=operation(num1,num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")
        if input(f"Type 'y' if you want to continue operations with {answer} or 'n' if you want to start a new operation: ")=="y":
            num1=answer
        else:
            to_continue=False
            calculator()
calculator()