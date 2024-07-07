print("Various option to perform some operations.")
print("1. ADD")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. MODULUS")

num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

options = int(input("enter any operation: "))
if(options==1):
    print("The total sum of num1 and num2 is : ", num1 + num2)
elif(options==2):
    print("The total subtraction of num1 and num2 is : ", num1 - num2)
elif(options==3):
    print("The total multiply of num1 and num2 is : ", num1 * num2)
elif(options==4):
    print("The total division of num1 and num2 is : ", num1 / num2)
elif(options==5):
    print("The total modulo of num1 and num2 is : ", num1 % num2)
else:
    print("invalid option choose.")
    


