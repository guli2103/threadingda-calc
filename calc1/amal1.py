import time

a = int(input("(12-3*2)+5 = "))
def amal1(a):
    if a == 11:
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")
        ochistva = input("Otangizni ismini kiriting: ")
        for x in range(30):
            time.sleep(0.2)
            print(ism,familiya,ochistva)  
    else:
        print("Javobingiz xato")        