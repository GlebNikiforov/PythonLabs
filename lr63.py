import random
import math

def PrintHelp():
    print("Possible operations: ")
    print("\thelp\t\tshow this message")
    print("\t+\t\tplus (for 2 numbers)")
    print("\t-\t\tminus (for 2 numbers)")
    print("\t/\t\tdivision (for 2 numbers)")
    print("\t*\t\tmultiply (for 2 numbers)")
    print("\t^\t\exponentiation (for 2 numbers)")
    print("\tabs\t\tabsolute value (for 1 number)")
    print("\trandom\t\trandom value from 0 to 1")
    print("\tfactorial\tfactorial (for 1 number)")
    print("\tacos\t\tarccosine (for 1 number)")
    print("\texit\t\tclose program")

def GetTwoFloatNumbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return (num1, num2)

def SumOperation():
    num1, num2 = GetTwoFloatNumbers()
    print("{} + {} = {}".format(num1, num2, num1 + num2))

def MinusOperation():
    num1, num2 = GetTwoFloatNumbers()
    print("{} - {} = {}".format(num1, num2, num1 - num2))

def DivisionOperation():
    num1, num2 = GetTwoFloatNumbers()
    print("{} - {} = {}".format(num1, num2, num1 - num2))

def MultiplyOperation():
    num1, num2 = GetTwoFloatNumbers()
    print("{} * {} = {}".format(num1, num2, num1 * num2))

def PowerOperation():
    num1, num2 = GetTwoFloatNumbers()
    print("{} ^ {} = {}".format(num1, num2, num1 ** num2))

def AbsoluteOperation():
    num = float(input("Enter number: "))
    print("|{}| = {}".format(num, abs(num)))

def RandomOperation():
    print("Random number: {}".format(random.random()))

def FactorialOperation():
    num = int(input("Enter number (only integers): "))
    print("{}! = {}".format(num, math.factorial(num)))

def AcosOperation():
    num = float(input("Enter number (from -1 to 1): "))
    print("acos({}) = {}".format(num, math.acos(num)))

def main():
    PrintHelp()
    while (True):
        operation = str(input("Enter an operation: "))
        if (operation == '+'):
            SumOperation()
        elif (operation == '-'):
            MinusOperation()
        elif (operation == '/'):
            DivisionOperation()
        elif (operation == '*'):
            MultiplyOperation()
        elif (operation == '^'):
            PowerOperation()
        elif (operation == 'abs'):
            AbsoluteOperation()
        elif (operation == 'random'):
            RandomOperation()
        elif (operation == 'factorial'):
            FactorialOperation()
        elif (operation == 'acos'):
            AcosOperation()
        elif (operation == 'help'):
            PrintHelp()
        elif (operation == 'exit'):
            break
        else:
            print("No such operator.")

main()