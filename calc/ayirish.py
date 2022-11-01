import time 

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
amal = input("Amalni kiriting: ")
def ayirish(a,b):
    if amal == "-":
        print("natijangiz: ",a-b )
        email = input("Emailingizni kiriting: ")
        parol = input("Parolni kiriting: ")
        for x in range(30):
            time.sleep(0.2)
            print(x)
