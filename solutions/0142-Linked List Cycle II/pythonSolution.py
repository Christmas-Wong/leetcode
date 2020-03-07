def hashSolution(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    visited = set()
    node = head
    while node is not None:
        if node in visited:
            return node
        else:
            visited.add(node)
            node = node.next
    return None

def fast_slow_pointer(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head