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
    public static class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
    }

    /**
     * 计算路径和
     * @param root
     * @param sum
     * @return
     */
    public static List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<Integer> list_1 = new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();
        pathSum(root, sum,list_1, result);
        return result;
    }

    /**
     * 计算路径和，方法重载
     * @param root
     * @param target
     * @param list_1
     * @param result
     */
    private static void pathSum(TreeNode root, int target, List<Integer> list_1, List<List<Integer>> result){
        if (root == null){
            return ;
        }
        list_1.add(root.val);
        if (root.left==null && root.right==null){
            if (root.val == target){
                result.add(new ArrayList<>(list_1));
            }
            return ;
        }
        if (root.left != null){
            pathSum(root.left, target-root.val, list_1, result);
            list_1.remove(list_1.size()-1);
        }
        if (root.right != null){
            pathSum(root.right, target-root.val, list_1, result);
            list_1.remove(list_1.size()-1);
        }
    }




    public static void main(String[] args) {
        TreeNode node01 = new TreeNode(5);
        TreeNode node02 = new TreeNode(4);
        TreeNode node03 = new TreeNode(8);
        TreeNode node04 = new TreeNode(11);
        TreeNode node05 = new TreeNode(13);
        TreeNode node06 = new TreeNode(4);
        TreeNode node07 = new TreeNode(7);
        TreeNode node08 = new TreeNode(2);
        TreeNode node09 = new TreeNode(5);
        TreeNode node10 = new TreeNode(1);

        node01.left = node02;
        node01.right = node03;

        node02.left = node04;

        node03.left = node05;
        node03.right = node06;

        node04.left = node07;
        node04.right = node08;

        node06.left = node09;
        node06.right = node10;

        System.out.println(pathSum(node01, 22));
    }
}
