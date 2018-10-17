#!/usr/bin/env python3
# -*- coding:utf-8 -*-

amount=int(input("Enter amount: "))

if amount <= 1000:
    discount=amount*0.05
    print("Discount 5%",discount)

elif amount <= 5000:
    discount=amount*0.10
    print("Discount 10%",discount)

else:
    discount = amount*0.15
    print("Discount 15%",discount)

print("Net payable:",amount-discount)
