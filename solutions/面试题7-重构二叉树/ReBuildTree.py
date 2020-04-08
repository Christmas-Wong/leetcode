class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder_traverse(head):
    if head is None:
        return None
    print(head.val)
    if head.left:
        preorder_traverse(head.left)
    if head.right:
        preorder_traverse(head.right)

def buildTree(preorder, inorder):
    if len(preorder) != len(inorder):
        return None
    if len(preorder)<1:
        return None
    root = TreeNode(preorder[0])
    root_index = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:root_index+1], inorder[0:root_index])
    root.right = buildTree(preorder[root_index+1:], inorder[root_index+1:])
    return root
preorder_list = [3,9,20,15,7]
inorder_list = [9,3,15,20,7]
head_node = buildTree(preorder_list, inorder_list)
preorder_traverse(head_node)