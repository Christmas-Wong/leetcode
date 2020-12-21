class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head):
    if not head or not head.next:
        return head
    pre, slow, fast = None, head, head
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    pre.next = None
    return merge_two_node(sort_list(head), sort_list(slow))


def merge_two_node(node_1, node_2):
    if not node_1 or not node_2:
        return node_2 if node_2 else node_1
    return_node = ListNode(0)
    tail_node = return_node
    while node_1 and node_2:
        if node_1.val < node_2.val:
            tail_node.next = node_1
            node_1 = node_1.next
        else:
            tail_node.next = node_2
            node_2 = node_2.next
        tail_node = tail_node.next
    tail_node.next = node_1 if node_1 else node_2
    return return_node.next


def print_node(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    node01 = ListNode(1)
    node02 = ListNode(3)
    node03 = ListNode(5)
    node04 = ListNode(4)
    node05 = ListNode(2)
    node06 = ListNode(0)

    node01.next = node02
    node02.next = node03
    node03.next = node04
    node04.next = node05
    node05.next = node06

    new_node = sort_list(node01)
    print_node(new_node)
