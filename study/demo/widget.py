# -*- coding: utf-8 -*-
import sys

"""
调试比例
"""


def test1():
    all_rem = 0
    per_rem = 0

    for i in range(0,10000,1):
        all_rem += 1
        rem = i%100
        # if rem :
        #     per_rem += 1
        print(str(i) + " " + str(rem))

    # print(all_rem)
    # print(per_rem)

    # print(per_rem/all_rem)

def test2():
    for i in range(1,100,1):
        print(str(i) + " " + str(i % 9))



test3()