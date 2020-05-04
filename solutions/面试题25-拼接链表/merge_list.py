
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_node(head):
    while head.next:
        print(head.val, end=", ")
        head = head.next
    print(head.val)


def merge_two_lists(head_1, head_2):
    output = head_out = ListNode(0)
    while head_1 and head_2:
        if head_1.val >= head_2.val:
            head_out.next = head_2
            head_2 = head_2.next
        else:
            head_out.next = head_1
            head_1 = head_1.next
        head_out = head_out.next

    head_out.next = head_1 or head_2

    return output.next


if __name__ == "__main__":
    node_11 = ListNode(1)
    node_12 = ListNode(11)
    node_13 = ListNode(21)
    node_14 = ListNode(31)
    node_15 = ListNode(41)
    node_16 = ListNode(50)

    node_11.next = node_12
    node_12.next = node_13
    node_13.next = node_14
    node_14.next = node_15
    node_15.next = node_16

    node_21 = ListNode(2)
    node_22 = ListNode(12)
    node_23 = ListNode(22)
    node_24 = ListNode(32)
    node_25 = ListNode(42)
    node_26 = ListNode(50)

    node_21.next = node_22
    node_22.next = node_23
    node_23.next = node_24
    node_24.next = node_25
    node_25.next = node_26

    print("***************************************")
    print("链表1：", end="")
    print_node(node_11)
    print("链表2：", end="")
    print_node(node_21)
    print("***************************************")
    print("上述两个链表拼接：", end="")
    print_node(merge_two_lists(node_11, node_21))