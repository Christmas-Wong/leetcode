class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    if n == 0:
        return head
    node_list = []
    while head:
        node_list.append(head)
        head = head.next
    if n == len(node_list):
        return node_list[1]
    if n == 1 and len(node_list) > 1:
        node_list[-2].next = None
        return node_list[0]
    if n == 1:
        return None
    index = len(node_list)-n-1
    node_list[index].next = node_list[index+2]
    return node_list[0]


def print_node(head):
    while head:
        print(head.val)
        head = head.next


def double_point(head, n):
    return_node = head
    pre_node = head
    i = 0
    while head:
        if i > n:
            pre_node = pre_node.next
        head = head.next
        i += 1
    if i == 1:
        return None
    if i == n:
        return return_node.next
    pre_node.next = pre_node.next.next
    return return_node


if __name__ == "__main__":
    node_01 = ListNode(1)
    node_02 = ListNode(2)
    # node_03 = ListNode(3)
    # node_04 = ListNode(4)
    # node_05 = ListNode(5)

    node_01.next = node_02
    # node_02.next = node_03
    # node_03.next = node_04
    # node_04.next = node_05

    # new_node = removeNthFromEnd(node_01, 2)
    new_node = double_point(node_01, 2)
    print_node(new_node)