import threading as th
import time

d = input('''Plasstik kartasi ochtirmoqchimisiz:
Ha
Yoq
''')
if d.lower() == "ha":
    from amal1 import *
    t1 = th.Thread(target=amal1(a))
    from amal2 import *
    t2 = th.Thread(target=amal2(b))
    from amal3 import *
    t3 = th.Thread(target=amal3(c))
    from amal4 import *
    t4 = th.Thread(target=amal4(g))

    t1.start()
    t2.start() 
    t3.start()
    t4.start()
    
elif d.lower() == "yoq":
    print("Sizga yordam berolmaymiz 20 soniya kuting")
    for x in range(1,21):
        time.sleep(1)
        print(x)


