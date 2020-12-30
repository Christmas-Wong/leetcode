import java.util.HashMap;
import java.util.Map;

public class main {
    static class TreeNode{
        private int val;
        private TreeNode left = null;
        private TreeNode right = null;
        TreeNode(int x){
            this.val = x;
        }
    }
    public static TreeNode buildTree(int[] preorder, int[] inorder){
        return createNode(0, 0, inorder.length-1, preorder, inorder);
    }
    public static TreeNode createNode(int root, int start, int end, int[] preorder, int[] inorder){
        if (root> preorder.length-1 || start>end){
            return null;
        }
        TreeNode rootNode = new TreeNode(preorder[root]);
        int index = 0;
        for (int i=start;i<=end;i++){
            if (preorder[root] == inorder[i]){
                index = i;
                break;
            }
        }
        rootNode.left = createNode(root+1, start, index-1, preorder, inorder);
        rootNode.right = createNode(root+index-start+1, index+1, end, preorder, inorder);
        return rootNode;
    }


    public static void main(String[] args){

    }
}
