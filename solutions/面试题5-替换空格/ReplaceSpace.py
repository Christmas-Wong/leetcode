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


def replace_space(strings):
    out_put = [item if item != " " else "%20" for item in strings]
    return "".join(out_put)


if __name__ == '__main__':
    s = "we are eating apple"
    print(replace_space(s))