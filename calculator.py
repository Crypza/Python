operator = input("Do you want to +, -, / or *?: ")

try:
    num1 = int(input("Enter a number here: "))
    num2 = int(input("Enter another number here: "))
except:
    print("Thats not a number >:C")
    exit()

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num1 == 0:
        print("You cant divide by 0")
        exit("Bye bye")
    elif num2 == 0:
        print("You cant divide by 0")
        exit("Bye bye")
    else:
        result = num1 / num2
#    result = num1 / num2
else:
    print("Error: not acceptable way of calculating")
    exit()

print(result)