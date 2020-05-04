
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_node(head):
    if head is None or head.next is None:
        return head
    temple_node = head.next
    pre_node = head
    if temple_node.next is None:
        head.next = None
        temple_node.next = head
        return temple_node
    while temple_node.next:
        post_node = temple_node.next
        temple_node.next = pre_node

        pre_node = temple_node
        temple_node = post_node
    temple_node.next = pre_node
    head.next = None
    return temple_node


def reverse_node_traverse(head):
    if head is None or head.next is None:
        return head
    mid_node = reverse_node_traverse(head.next)
    head.next.next = head
    head.next = None
    return mid_node


def print_node(head):
    while head.next:
        print(head.val, end="")
        head = head.next
    print(head.val)


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    print("*****************************")
    print("链表初始化结构：", end="")
    print_node(node_1)
    print("*****************************")
    print("常规第一次反转链表：", end="")
    print_node(reverse_node(node_1))
    print("*****************************")
    print("递归第二次反转链表：", end="")
    print_node(reverse_node_traverse(node_6))