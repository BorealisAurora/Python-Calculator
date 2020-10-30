#Import "time.sleep(n)"
import time

#Define functions
def subtract(num1,num2):
    return num1 - num2

def add(num1,num2):
    return num1 + num2

def divide(num1,num2):
    return num1 / num2

def multiply(num1,num2):
    return num1 * num2

def main():
    time.sleep(1)
    print("Select an operation from the list below:")
    time.sleep(1)
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Divison")
    choice = input("Enter choice (1,2,3,4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(num1, "+", num2,"=", add(num1,num2))
        time.sleep(1)
        restart = input("Restart? (y/n): ")

    if choice == "2":
        print(num1, "-", num2,"=", subtract(num1,num2))
        time.sleep(1)
        restart = input("Restart? (y/n): ")

    if choice == "3":
        print(num1, "*", num2,"=", multiply(num1,num2))
        time.sleep(1)
        restart = input("Restart? (y/n): ")

    if choice == "4":
        print(num1, "/", num2,"=", divide(num1,num2))
        time.sleep(1)
        restart = input("Restart? (y/n): ")

    if restart == "y" or "yes":
        main()

    if restart == "n" or "no":
        exit()

#Run the "main" function
main()
