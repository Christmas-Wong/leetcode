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


def frog_step_recursive(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    return frog_step_recursive(num-1)+frog_step_recursive(num-2)


def frog_step_DP(num):
    mid_list = [1, 2]
    for index in range(2, num):
        mid_list.append(mid_list[index-1] + mid_list[index-2])
    return mid_list[-1]


def frog_step_DP_optimized(num):
    mid_num_1 = 1
    mid_num_2 = 2
    for index in range(3, num+1):
        mid_num_3 = mid_num_1
        mid_num_1 = mid_num_2
        mid_num_2 = mid_num_3 + mid_num_1
    return mid_num_2


if __name__ == '__main__':
    number = 7
    print("递归解法：青蛙跳上第{}台阶有{}方式".format(str(number), str(frog_step_recursive(number))))
    print("DP解法：青蛙跳上第{}台阶有{}方式".format(str(number), str(frog_step_DP(number))))
    print("优化后的DP解法：青蛙跳上第{}台阶有{}方式".format(str(number), str(frog_step_DP_optimized(number))))

