class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_kth_from_end(head, k):
    if head is None or k < 0:
        return None
    counter = 0
    temple = head
    while head.next:
        head = head.next
        if counter >= k-1:
            temple = temple.next
        counter += 1
    if counter < k-1:
        return None
    return temple.val


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)
    node_7 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    print(get_kth_from_end(node_1, 8))