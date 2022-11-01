import time

c = int(input("33-8/4+3*2 = "))
def amal3(c):
    if c == 37:
        s = int(input('''Qanaqa plasstik ochtirmoqchisiz:
        1:Humo
        2:Uzcard
        '''))
        if s == 1:
            print("Siz Humo plasstik kartasini tanladingiz ")
            pas = input("Pasport seriyangizni kiriting: ")
            tel = int(input("Telefon raqamingizni kiriting: "))
            for x in range(30):
                time.sleep(0.2)
                print(pas,tel)
            print("Tabriklaymiz siz Humo plassik kartasini ochdingiz")
        elif s == 2:
            print("Siz Uzcard plasstik kartasini tanladingiz ")
            pas = input("Pasport seriyangizni kiriting: ")
            tel = int(input("Telefon raqamingizni kiriting: "))         
            for x in range(30):
                time.sleep(0.2)
                print(pas,tel)
            print("Tabriklaymiz siz Uzcard plassik kartasini ochdingiz")

    else:
        print("Javobingiz xato")        