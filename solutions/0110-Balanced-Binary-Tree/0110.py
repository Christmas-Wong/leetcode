# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        return abs(left_depth-right_depth)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
def depth(head):
    if head is None:
        return 0
    return max(depth(head.left), depth(head.right))+1