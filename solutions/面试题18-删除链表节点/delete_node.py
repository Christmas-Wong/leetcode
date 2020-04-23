class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def node_reader(header):
    print(header.val)
    if header.next:
        node_reader(header.next)


def delete_val(header, num):
    if header is None:
        return None
    if header.val == num:
        return header.next if header.next else None
    output = header
    while header and header.next:
        next_node = header.next
        if next_node.val == num:
            if next_node.next:
                header.next = next_node.next
            else:
                header.next = None
        header = header.next
    return output


def delete_node(header, node):
    if header is node:
        if header.next:
            return header.next
        return None
    if node.next:
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
    else:
        new_node = header
        while new_node.next.next:
            new_node.next = new_node.next
            new_node = new_node.next
        new_node.next = None
    return header


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    node_reader(node_1)
    print("**************************")
    # node_reader(delete_val(node_1, 1))
    node_reader(delete_node(node_1, node_5))
