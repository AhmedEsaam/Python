import platform
import BIT_MATH

MyName = input ("Please Enter your Name: ")
MyBirthDate = input ("Please Enter your Birth Date: ")
MyFaculty = input ("Please Enter your Faculty: ")

f1 = open("file.txt", "a+")
f1.write("Your Name: " + MyName + "\n")
f1.write("Your Birth Date: " + MyBirthDate + "\n")
f1.write("Your Faculty: " + MyFaculty + "\n")

f1 = open("file.txt", "r")
print(f1.read())