print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. DIVIDE")
print("4. MULTIPY")
print("5. MODULUS")

operation = input("Enter option: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "1":
    
    print("The result is " + str(int(num1) + int(num2)))
elif operation == "2":

    print("The result is " + str(int(num1) - int(num2)))
elif operation == "3":
    if num2 == 0.0:
        print("Divide by 0 Error")
    else:
        print("The result is " + str(int(num1) / int(num2)))
elif operation == "4":
   
    print("The result is " + str(int(num1) * int(num2)))
elif operation == "5":
    
    print("The result is " + str(int(num1) % int(num2)))
else:
    print("Invalid option")

   
