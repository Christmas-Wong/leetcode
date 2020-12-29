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



def isBalanced(self, root):
    return dfs_height(root) != -1
def dfs_height(head):
    if head is None:
        return True
    left_height = dfs_height(head.left)
    if left_height == -1:
        return -1
    right_height = dfs_height(head.right)
    if right_height == -1:
        return -1
    return max(left_height, right_height)+1