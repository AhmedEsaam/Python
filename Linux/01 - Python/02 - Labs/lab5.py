my_set = (input("please enter 5 numbers: ").split(','))

num = (input("please enter the your number: "))

if num in my_set:
    print("number exists")
else:
    print("number does not exist")