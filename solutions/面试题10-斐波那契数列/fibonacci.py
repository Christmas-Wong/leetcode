#!/usr/bin/env python
# encoding: utf-8
"""
@author: WangFei
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@contact: wf18684531169@gmail.com
@software: pycharm
@file: HomeWork.py
@time: 2020/3/15 17:39
@desc
"""


def fibonacci_recursive(end_num):
    if end_num == 1 or end_num == 2:
        return 1
    return fibonacci_recursive(end_num-1) + fibonacci_recursive(end_num-2)


def fibonacci_dp(end_num):
    if end_num == 1 or end_num == 2:
        return 1
    fibonacci_list = [1, 1]
    for item in range(2, end_num):
        fibonacci_list.append(fibonacci_list[item-1]+fibonacci_list[item-2])
    return fibonacci_list[-1]


if __name__ == '__main__':
    print(fibonacci_recursive(10))
    print(fibonacci_dp(10))
