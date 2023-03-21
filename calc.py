print("Choose Operation to be execute: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Choice No. : ")
if operation == "1" :
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second number: "))
    print("The sum of the number is: " + str(float(num1)+float(num2)))
elif operation == "2":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second number: "))
    print("The difference of the number is: " + str(float(num1) - float(num2)))
elif operation == "3" :
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second number: "))
    print("The product of the number is: " + str(float(num1) * float(num2)))
elif operation == "4" :
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second number: "))
    print("The difference of the number is: " + str(float(num1) - float(num2)))
else:
    print("!!Invalid input!!")