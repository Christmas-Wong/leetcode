# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return separate_two_list(lists, 0, len(lists)-1)

def separate_two_list(lists, start, end):
    if start > end:
        return None
    if start == end:
        return lists[start]
    mid = (start + end)>>1
    return merge_two_list(separate_two_list(lists, start, mid), separate_two_list(lists, mid+1, end))


def merge_two_list(list_1, list_2):
    if not list_1 or not list_2:
        return list_2 if list_1 is None else list_1
    head_1 = list_1
    head_2 = list_2
    return_head = ListNode(0)
    tail_node = return_head
    while head_1 and head_2:
        if head_1.val > head_2.val:
            tail_node.next = head_2
            head_2 = head_2.next
        else:
            tail_node.next = head_1
            head_1 = head_1.next
        tail_node = tail_node.next
    tail_node.next = head_1 if head_1 else head_2
    return return_head.next