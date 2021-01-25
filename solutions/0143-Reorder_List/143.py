class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def re_order_list(head):
    if not head or not head.next:
        return head
    node_list = []
    while head:
        node_list.append(head)
        head = head.next
    count = len(node_list)-1
    i = 0
    connect_node = ListNode(-1)
    while i < count-i:
        connect_node.next = node_list[i]
        node_list[i].next = node_list[count-i]
        connect_node = node_list[count-i]
        i += 1
    if i == count-i:
        connect_node.next = node_list[i]
    node_list[i].next = None

    return node_list[0]


def print_list(start):
    if not start:
        return None
    print(start.val)
    print_list(start.next)


if __name__ == "__main__":
    node01 = ListNode(1)
    node02 = ListNode(2)
    node03 = ListNode(3)
    node04 = ListNode(4)
    # node05 = ListNode(5)

    node01.next = node02
    node02.next = node03
    node03.next = node04
    # node04.next = node05

    print_list(node01)

    print("*"*6)

    new_node = re_order_list(node01)

    print_list(new_node)