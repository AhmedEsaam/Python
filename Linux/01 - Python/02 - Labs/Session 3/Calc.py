
while(1):

    query = input()
    calc = query.split()

    num1 = int(calc[0])
    operation = calc[1]
    num2 = int(calc[2])

    result = 0

    if (operation == "+"):
        result = num1 + num2
        print(result)
    elif (operation == "-"):
        result = num1 - num2
        print(result)
    elif (operation == "*"):
        result = num1 * num2
        print(result)
    elif (operation == "/"):
        result = num1 / num2
        print(result)

    f1 = open("CalcHistory.txt", "a+")

    f1.write(str(num1) + " " + (operation) + " " + str(num2) + " "  + "\n")
    f1.write(str(result) + "\n")

    operation = ''
    f1.close()




f1 = open("CalcHistory.txt", "r")
print(f1.read())
