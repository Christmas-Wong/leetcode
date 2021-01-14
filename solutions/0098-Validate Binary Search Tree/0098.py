class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return judge(root, float("inf"), float("-inf"))
    
def judge(root, max_val, min_val):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return judge(root.left, min(max_val, root.val), min_val) and judge(root.right, max_val, max(min_val, root.val))
