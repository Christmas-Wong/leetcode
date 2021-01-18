import tensorflow as tf


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    status = 0
    start = return_node = ListNode(0)
    while l1 and l2:
        num = l1.val + l2.val + status
        status = 0
        new_node = ListNode(num)
        if num > 9:
            new_node = ListNode(num-10)
            status = 1
        start.next = new_node

        start = start.next
        l1 = l1.next
        l2 = l2.next
    mid_node = None
    if l1:
        mid_node = l1
    if l2:
        mid_node = l2
    while mid_node and status:
        num = mid_node.val + status
        status = 0
        new_node = ListNode(num)
        if num > 9:
            new_node = ListNode(num-10)
            status = 1
        start.next = new_node

        start = start.next
        mid_node = mid_node.next
    if mid_node:
        start.next = mid_node
    if status == 1:
        start.next = ListNode(1)
    return return_node.next

def print_list(node_list):
    while node_list:
        print(node_list.val)
        node_list = node_list.next



if __name__ == "__main__":
    node01 = ListNode(9)
    node02 = ListNode(9)
    node03 = ListNode(1)
    node01.next = node02
    node02.next = node03

    node04 = ListNode(1)

    node = add_two_numbers(node01, node04)
    print_list(node)
