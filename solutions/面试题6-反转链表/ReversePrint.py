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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_print_stack(head):
    """
    :type head: ListNode
    :rtype: List[int]
    """
    output = []
    while head.next:
        output.append(head.val)
        head = head.next
    output.append(head.val)
    for i in range(len(output)-1, -1, -1):
        print(output[i])


def reverse_print_recursive(head):
    if head.next:
        reverse_print_recursive(head.next)
    print(head.val)


if __name__ == '__main__':
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    reverse_print_stack(node_1)
    reverse_print_recursive(node_1)
