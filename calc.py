import pyttsx3 as pt
import time
import os
#----------------------------------------------
pt.speak("Hiii KP !!!")
pt.speak("I am your Voice Enabled Calculator")
print()
print("                                                    --------------------")
print("					       	       | Welcome KP |")
print("                                                    --------------------")
pt.speak("I can do the following arithmetic operations for you .")

#--------------------------------------------------

pt.speak("Press")
print("		Press")
pt.speak("1 to perform addition")
print("  1 : Addition")
time.sleep(1)
pt.speak("2 to perform subtraction")
print("  2 : Subtraction")
time.sleep(1)
pt.speak("3 to perform multiplication")
print("  3 : Multiplication")
time.sleep(1)
pt.speak("4 to perform division")
print("  4 : Division")
time.sleep(1)
pt.speak("5 to get remainder")
print("  5 : Remainder")
time.sleep(1)
pt.speak("6 to calculate power")
print("  6 : Power")
time.sleep(1)
pt.speak("7 to exit from the program")
print("  7 : Exit")
time.sleep(2)

#--------------------------------------
while True:
    
    pt.speak("		So Enter your choice according to which operation you wanna do : ")
    print("		Enter your choice : " , end="")
    n = int(input())
    if n > 7:
        pt.speak("Wronng Choice Bro .. try again")
        print("		Wronng Choice Bro")
        pt.speak(" So enter your choice according to which operation you wanna do : ")
        print("		Enter your choice : " , end="")
        n = int(input())
    if n == 7:
        pt.speak("Bye Bye KP")
        print("		Bye Bye KP")
        break
        exit()
#---------------------------------------------------------
    pt.speak("Please enter Your First Number")
    print("		Please enter Your First Number : " , end="")
    a = input()

    pt.speak("Please enter Your Second Number")
    print("		Please enter Your Second Number : " , end="")
    b = input()
#--------------------------------------------------------------
    if "." in a:
        a = float(a)
    else:
        a = int(a)
#------------------------
    if "." in b:
        b = float(b)
    else:
        b = int(b)
#---------------------------------------------------------
    if n == 1:
        result = a+b
        pt.speak(result)
        print(result)
        time.sleep(2)
    elif n == 2:
        result = a-b
        pt.speak(result)
        print(result)
        time.sleep(2)
    elif n == 3:
        result = a*b
        pt.speak(result)
        print(result)
        time.sleep(2)
    elif n == 4:
        result = a/b
        pt.speak(result)
        print(result)
        time.sleep(2)
    elif n == 5:
        result = a%b
        pt.speak(result)
        print(result)
        time.sleep(2)
    elif n == 6:
        result = a**b
        pt.speak(result)
        print(result)
        time.sleep(2)
    else:
        pt.speak("Wronng Choice Bro")
        print("Wronng Choice Bro")
    time.sleep(2)
    os.system("cls")
    print()
    print("                                                    --------------------")
    print("					       	       | Welcome KP |")
    print("                                                    --------------------")

    print("		Press")
    print("  1 : Addition")
    print("  2 : Subtraction")
    print("  3 : Multiplication")
    print("  4 : Division")
    print("  5 : Remainder")
    print("  6 : Power")
    print("  7 : Exit")
    time.sleep(1)
time.sleep(2)        
