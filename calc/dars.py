import threading as th
import time

print('''Institutimizga xush kelibsiz''')

from qoshish import *
t1 = th.Thread(target=qoshish(a,b))
t1.start() 
print("10 soniya kuting:")
for x in range(11):
    time.sleep(1)
    print(x)
   

from bolish import *
t2 = th.Thread(target=bolish(a,b))
t2.start()
print("10 soniya kuting:")
for x in range(11):
    time.sleep(1)
    print(x)

from kopaytirish import *
t3 = th.Thread(target=kopaytirish(a,b))
t3.start()
print("10 soniya kuting:")
for x in range(11):
    time.sleep(1)
    print(x)

from ayirish import *
t4 = th.Thread(target=ayirish(a,b))
t4.start()
print("10 soniya kuting:")
for x in range(11):
    time.sleep(1)
    print(x)