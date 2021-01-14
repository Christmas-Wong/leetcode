# -*- coding: utf-8 -*-
"""
@Time    : 2020/12/4 9:01
@Author  : Fei Wang
@File    : main
@Software: PyCharm
@Description: 
"""


class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_k_group(start, k):
    if not start or k < 2:
        return start
    node = start
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    if count < k:
        return start
    pre, new_start = reverse_node(start, k)
    start.next = reverse_k_group(new_start, k)
    return pre


def reverse_node(start, k):
    if not start:
        return start
    pre = None
    cur = start
    while cur and k > 0:
        cur.next, pre, cur = pre, cur, cur.next
        k -= 1
    return pre, cur


def print_node(start):
    if not start:
        return
    print(start.val)
    print_node(start.next)


if __name__ == "__main__":
    node01 = Node(1)
    node02 = Node(2)
    node03 = Node(3)
    node04 = Node(4)
    node05 = Node(5)
    node06 = Node(6)

    node01.next = node02
    node02.next = node03
    node03.next = node04
    node04.next = node05
    node05.next = node06

    print_node(node01)
    new_node = reverse_k_group(node01, 3)
    print_node(new_node)
