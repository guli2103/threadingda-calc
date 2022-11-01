import time

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
amal = input("Amalni kiriting: ")
def bolish(a,b):
    if amal == "/":
        print("natijangiz:",a / b)
        yosh = int(input("yoshingizni kiriting: "))
        if yosh <= 15:
            print("Siz hali passport olmagansiz shu sababli bizning institutimizga kirolmaysiz")
        elif yosh >= 16:
            print("Siz yoshingizga to'lgansiz institumizga kirish uchun test topshiriqlarini kuting")
        elif yosh >= 50:
            print("Sizning yoshingiz kattalik qiladi ")
            for x in range(30):
                time.sleep(0.2)
                print(x)    
                    



    

