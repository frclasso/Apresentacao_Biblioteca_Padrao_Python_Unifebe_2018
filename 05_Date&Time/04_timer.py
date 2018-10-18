#!/usr/bin/env python3

# Create a timer

import time

#exemplo 1
import time

print("Start:  %s" % time.ctime())

time.sleep(5)
print("End:  %s" % time.ctime())


# exemplo 2
run = input("Start? >")

seconds = 0

if run == "yes":
    while seconds !=6:
        print(">",seconds)
        time.sleep(1) # tempo de espera
        seconds+=1
print('Finish')


