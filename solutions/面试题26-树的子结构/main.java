import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class main {

    /**
     * Definition for a binary tree node.
     */
      public static class TreeNode {
          int val;
          TreeNode left;
          TreeNode right;
          TreeNode(int x) { val = x; }
      }

    public boolean isSubStructure(TreeNode A, TreeNode B) {
        return (A != null && B != null) && (recur(A, B) || isSubStructure(A.left, B) || isSubStructure(A.right, B));
    }
    boolean recur(TreeNode A, TreeNode B) {
        if(B == null) return true;
        if(A == null || A.val != B.val) return false;
        return recur(A.left, B.left) && recur(A.right, B.right);
    }



    public static void main(String[] args) {
        TreeNode node01 = new TreeNode(1);
        TreeNode node02 = new TreeNode(0);
        TreeNode node03 = new TreeNode(1);
        TreeNode node04 = new TreeNode(-4);
        TreeNode node05 = new TreeNode(-3);

        node01.left = node02;
        node01.right = node03;

        node02.left = node04;
        node02.right = node05;

        TreeNode node06 = new TreeNode(1);
        TreeNode node07 = new TreeNode(-4);

        node06.left = node07;

        System.out.println(isSubStructure(node01, node02));

    }
}
