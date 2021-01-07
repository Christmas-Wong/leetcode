import java.util.*;

/**
 * @Author Wang Fei
 * @Date 2020/12/3 15:51
 * @Version 1.0
 */
public class main {
    /**
     * Definition for a binary tree node.
     */
    private static int maxValue;

    public static class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
    }

    public static int maxPathSum(TreeNode root){
        maxValue = Integer.MIN_VALUE;
        return 0;
    }

    public static int maxDown(TreeNode node){
        if (node == null){
            return 0;
        }
        int leftValue = Math.max(0, maxDown(node.left));
        int rightValue = Math.max(0, maxDown(node.right));
        int sumResult = leftValue + rightValue + node.val;
        maxValue = Math.max(sumResult, maxValue);
        return Math.max(leftValue, rightValue)+node.val;

    }

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
