# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rightSideView(self, node):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not node:
            return node
        status = False
        # status is true for list_a
        list_a = []
        # status is false for list_b
        list_b = []
        list_a.append(node)
        return_list = []
        while len(list_a) > 0 or len(list_b) > 0:
            new_node = None
            if not status:
                new_node = list_a[0]
                list_a.remove(new_node)
                if new_node.left:
                    list_b.append(new_node.left)
                if new_node.right:
                    list_b.append(new_node.right)
                if len(list_a) == 0:
                    return_list.append(new_node.val)
                    status = True
            else:
                new_node = list_b[0]
                list_b.remove(new_node)
                if new_node.left:
                    list_a.append(new_node.left)
                if new_node.right:
                    list_a.append(new_node.right)
                if len(list_b) == 0:
                    return_list.append(new_node.val)
                    status = False

        return return_list