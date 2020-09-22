import pickle
import pathlib
import winsound
import pyttsx3
import re
import os
from emailchecker import emailchecker
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
def colorText(text):
    for color in COLORS:
        text = text.replace(color, COLORS[color])
    return text
class Ac:
    acnm =0
    name=''
    type=''
    deposit=0
    def Newac(self):
        emailchecker.speak("please enter your name")
        self.name=input("\t\tenter name :")
        while self.name=="":
            en.say("please enter your name")
            en.runAndWait()
            self.name=input("\t\tenter your name")
        emailchecker.speak("please enter your mail id")
        self.mail=input("\t\tPlease enter your mail id")
        self.mail=emailchecker.AcVerifier1(self.mail)
        emailchecker.speak("please enter your mobile number")
        self.mobile=input("\t\tplease enter your mobile number")
        self.mobile=emailchecker.AcVerifier2(self.mobile)
        print("\t\t1.Current AC")
        print("\t\t2.Savings AC")
        emailchecker.speak("please choose an option")
        i=''
        i=input("\t\tchoose an option")
        while i!='1' and i!='2':
            winsound.MessageBeep()
            emailchecker.speak("please choose correct option")
            i=input("\t\tplease choose correct option")
        if i == '1':
            self.type = 'Current'
        elif i == '2':
            self.type = 'Savings'
        if self.type=='Current':
            emailchecker.speak("please enter amount to deposit not less than 5000")
            self.deposit = int(input("\t\tEnter amount to Deposit >=5000"))
            emailchecker.deposit(self.deposit)
        else:
            emailchecker.speak("please enter amount to deposit")
            self.deposit=int(input("\t\tenter amount to deposit"))
        emailchecker.speak("please enter account number")
        self.acnm=int(input("\t\tenter account number"))
        self.acnm=emailchecker.AcVerifier3(self.acnm)

def intr():
    emailchecker.speak("welcome to Mini Bank")
    with open('font1.txt','r') as f:
        a="".join(f.readlines())
        print(colorText(a))
def newac():
    ac=Ac()
    ac.Newac()
    writeAc(ac)
def writeAc(ac):
    file = pathlib.Path("bank.data")
    if file.exists():
        infile = open('bank.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(ac)
        infile.close()
    else:
        oldlist = [ac]
    outfile = open('bank.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
def depositAndWith(A,B):
    path=pathlib.Path("bank.data")
    if path.exists():
        with open("bank.data","rb") as f:
            data=pickle.load(f)
            for item in data:
                if B==1:
                    if item.acnm==A:
                        emailchecker.speak("please enter amount to depsoit")
                        amount=int(input("\t\tenter deposit amount"))
                        item.deposit+=amount
                        emailchecker.speak("your amount deposited successfully")
                        print("\t\tyour account balance :",item.deposit)
                        break
                    else:
                        print("no")
                elif B==2:
                    if item.acnm==A:
                        emailchecker.speak("please enter amount to withdrawl")
                        amount = int(input("\t\tenter amount to withdrawl"))
                        if item.type=='Current':
                            if item.deposit<=5000 or item.deposit-amount==5000:
                                emailchecker.speak("Sorry your amount is low to withdrawl")
                                print("\t\tno amount to withdrawl in your account")
                            else:
                                item.deposit-=amount
                        elif item.deposit<amount:
                            emailchecker.speak("Sorry your amount is low")
                            print("\t\tSorry your amount is low")
                        else:
                            item.deposit =item.deposit-amount
                            print("\t\t your account balance :",item.deposit)
                            break
                else:
                    emailchecker.speak("no records found")
                    print("\t\tno records found")
    with open("bank.data","wb") as f:
        pickle.dump(data,f)
def modify(acc):
    path=pathlib.Path("bank.data")
    if path.exists():
        with open("bank.data","rb") as f:
            data=pickle.load(f)
            for item in data:
                if item.acnm==acc:
                    print("\t\t1.Name");
                    print("\t\t2.type")
                    print("\t\t3.Mailid")
                    print("\t\t4.Mobile")
                    emailchecker.speak("please choose an option to modify")
                    inp = input("\t\tplease choose an option to modify")
                    if inp=='1':
                        emailchecker.speak("please enter your name")
                        item.name=input("\t\tenter name to modify")
                        emailchecker.speak("your name modified successfully")
                    elif inp=='2':
                        print("\t\t1.Current AC")
                        print("\t\t2.Savings AC")
                        emailchecker.speak("please choose an option")
                        i = int(input("\t\tchoose any option"))
                        while i > 2:
                            emailchecker.speak("please choose correct option")
                            i = int(input("\t\tplease choose correct option"))
                        if i == 1:
                            item.type = 'Current'
                        elif i == 2:
                            item.type = 'Savings'
                        if item.type == 'Current':
                            if item.deposit<5000:
                                emailchecker.speak("to get current account minimum balance should be 5000")
                                deposit=int(input("\t\tenter amount to deposit"))
                                item.deposit+=deposit
                                while item.deposit<5000:
                                    j=5000-item.deposit
                                    emailchecker.speak("your account balance must be 5000")
                                    print("\t\tyour account balance is :",item.deposit)
                                    deposit=int(input("\t\tdeposit {} to get current account".format(5000-item.deposit)))
                                    item.deposit+=deposit
                                emailchecker.speak("your account modified successfully")
                                print("\t\tyour account balance :",item.deposit)
                                break
                            else:
                                break
                    elif inp=='3':
                        emailchecker.speak("Please enter your mail id ")
                        item.mail=input("\t\tplease enter your mail id")
                        item.mail=emailchecker.AcVerifier1(item.mail)
                        break
                    elif inp=='4':
                        emailchecker.speak("Please enter your mobile number")
                        item.mobile=input("\t\tPlease enter your mobile number")
                        item.mobile=emailchecker.AcVerifier2(item.mobile)
                        break
                    else:
                        emailchecker.speak("please enter a valid option")
                        print("enter valid option")
                        modify(acc)

    else:
        emailchecker.speak("sorry no records found")
        print("no records found")
    with open("bank.data","wb") as f:
        pickle.dump(data,f)
def display(acc):
    path=pathlib.Path("bank.data")
    if path.exists():
        with open("bank.data","rb") as f:
            data=pickle.load(f)
            for item in data:
                if item.acnm==acc:
                    emailchecker.speak("your account details")
                    print("\t\tYour Account Details")
                    print("\t\tName :",item.name)
                    print("\t\tAC no :",item.acnm)
                    print("\t\tAC type :",item.type)
                    print("\t\tAccount Balance :",item.deposit)
                    print("\t\tMail id :",item.mail)
                    print("\t\tmobile number:",item.mobile)
def displayAll():
    path=pathlib.Path("bank.data")
    if path.exists():
        with open("bank.data","rb") as f:
            data=pickle.load(f)
            for item in data:
                print("\t\tAcNO:\t",item.acnm,"\tName:",item.name,"\tAcType:",item.type,"\tAcBalance:",item.deposit,"\tMail id:",item.mail,"\tMobile:",item.mobile)
    else:
        print("\t\tno records found")
def DelAc(acc):
    path=pathlib.Path("bank.data")
    if path.exists():
        with open("bank.data","rb") as f:
            data=pickle.load(f)
            newdata=[]
            for item in data:
                if item.acnm!=acc:
                    newdata.append(item)
    else:
        print("\t\tno records found")
    with open("bank.data","wb") as f:
        pickle.dump(newdata,f)
    emailchecker.speak("your account deleted successfully")
    print("\t\tyour account is deleted ")
b=''
intr()
while b!='9':
    print("\t\t1.New Account")
    print("\t\t2.Deposit")
    print("\t\t3.Withdrawl")
    print("\t\t4.Modify Account")
    print("\t\t5.Delete Account")
    print("\t\t6.Display your Account details ")
    print("\t\t7.Display All Account Holders")
    print("\t\t8.Exit")
    emailchecker.speak("please select an option")
    a = input("\t\tplease select an option")
    if a=='1':
        newac()
    elif a=='2':
        emailchecker.speak("please enter your account number")
        acc=int(input("\t\tEnter your A/C number to deposit "))
        depositAndWith(acc,1)
    elif a=='3':
        emailchecker.speak("Enter your Account number to withdrawl")
        acc=int(input("\t\tEnter your A/C number to withdrawl"))
        depositAndWith(acc,2)
    elif a=='4':
        emailchecker.speak("Enter your Account number to modify")
        acc=int(input("\t\tEnter your A/C number to modify"))
        modify(acc)
    elif a=='5':
        emailchecker.speak("Enter your Account number to delete")
        acc=int(input("\t\tEnter your A/C number to delete "))
        DelAc(acc)
    elif a=='6':
        emailchecker.speak("Enter your Account number to get details")
        acc=int(input("\t\tEnter your A/C number to get details"))
        display(acc)
    elif a=='7':
        displayAll()
    elif a=='8':
        emailchecker.speak("Thanks for using our service")
        print("\t\tThanks for using our service")
        b='8'
    elif a=='9':
        delall()
    else:
        winsound.MessageBeep()
        emailchecker.speak("please enter correct option")
        winsound.MessageBeep()
    emailchecker.speak("press any button")
    print(input())






