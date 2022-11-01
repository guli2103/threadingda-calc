import time

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
amal = input("Amalni kiriting: ")
def qoshish(a,b):
    if amal == "+":
        print("natijangiz:", a + b)
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")
        ochistva = input("Otangizni ismini kiriting: ")
        for x in range(30):
            time.sleep(0.2)
            print(ism,familiya,ochistva)

