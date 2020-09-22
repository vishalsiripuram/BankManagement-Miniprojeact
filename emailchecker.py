import re
import pyttsx3
import pickle
import pathlib
def speak(content):
    en = pyttsx3.init()
    voices = en.getProperty('voices')
    en.setProperty('rate', 125)
    voices = en.setProperty('voice', voices[1].id)
    en.say(content)
    en.runAndWait()
def AcVerifier3(num1):
    path=pathlib.Path("bank.data")
    if path.exists():
        with open("bank.data", "rb") as f:
            data = pickle.load(f)
            for item in data:
                B = True
                while item.acnm == num1:
                    speak("your account number is already existed")
                    print("\t\tyour account number is already existed")
                    num1 = int(input("\t\tplease enter new A/C number"))
                    AcVerifier3(num1)
    return num1

def deposit(depositm):
    while depositm < 5000:
        speak("please enter amount to deposit not less than 5000")
        depositm = int(input("\t\tenter amount >5000"))
    en.say("your amount deposited successfully")
    en.runAndWait()
    return depositm
def AcVerifier1(num1):
    if path.exists():
        with open("bank.data", "rb") as f:
            data = pickle.load(f)
            for item in data:
                B = True
                while B:
                    if re.search(MailCheck, num1):
                        B = False
                    else:
                        speak("please enter a valid mail id")
                        num1 = input("\t\tPlease enter valid mail id")
                while item.mail == num1:
                    speak("Your mail id is already existed please enter new mail id")
                    print("\t\tyour mail id is already existed")
                    num1= input("\t\tplease enter new mail id")
                    AcVerifier1(num1)
    return num1
def AcVerifier2(num2):
    if path.exists():
        with open("bank.data", "rb") as f:
            data = pickle.load(f)
            for item in data:
                A = True
                while A:
                    if re.search(Mobilecheck, num2) and len(num2) == 10:
                        A = False
                    else:
                        speak("Please enter valid mobile number")
                        num2 = input("\t\tPlease enter valid mobile number")
                while item.mobile == num2:
                    speak("Your mobile number is already existed please enter new mobile number")
                    print("\t\tyour mobile number is already existed")
                    num2 = input("\t\tplease enter new mobile number")
                    AcVerifier2(num2)
    return num2
path=pathlib.Path("bank.data")
MailCheck = '^[_0-9a-zA-Z]+(\.[a-zA-Z0-9]+)*@[a-z]+(\.[a-zA-Z]+)*(\.[a-z]{2,4})$'
Mobilecheck = "^[0-9]+[0-9]$"
if __name__=='main':
    AcVerifier1(num)
    AcVerifier2(num)
    AcVerifier3(num)
    deposit(depositm)


