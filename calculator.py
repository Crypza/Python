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
    try:
        result = num1 / num2
    except ZeroDivisionError:
        exit("You cant divide by 0")
else:
    exit("Error: not acceptable way of calculating")

print(result)