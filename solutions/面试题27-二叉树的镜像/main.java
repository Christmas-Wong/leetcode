import com.sun.deploy.util.StringUtils;

import java.util.*;
import java.util.stream.Collectors;

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

    private static TreeNode mirrorTree(TreeNode root){
        if (root == null){
            return null;
        }
        Stack<TreeNode> nodeStack = new Stack<>();
        nodeStack.add(root);
        while (!nodeStack.isEmpty()){
            TreeNode popNode = nodeStack.pop();
            if (popNode.right != null){
                nodeStack.add(popNode.right);
            }
            if (popNode.left != null){
                nodeStack.add(popNode.left);
            }
            TreeNode leftNode = popNode.left;
            popNode.left = popNode.right;
            popNode.right = leftNode;

        }
        return root;
    }

    private static void printTree(TreeNode root){
        if(root == null)
        {
            return ;
        }
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        TreeNode current = null;
        queue.offer(root);//将根节点入队
        while(!queue.isEmpty())
        {
            current = queue.poll();//出队队头元素并访问
            System.out.print(current.val + " ");
            if(current.left != null)//如果当前节点的左节点不为空入队
            {
                queue.offer(current.left);
            }
            if(current.right != null)//如果当前节点的右节点不为空，把右节点入队
            {
                queue.offer(current.right);
            }
        }



    }

    public static void main(String[] args) {
        TreeNode node01 = new TreeNode(4);
        TreeNode node02 = new TreeNode(2);
        TreeNode node03 = new TreeNode(7);
        TreeNode node04 = new TreeNode(1);
        TreeNode node05 = new TreeNode(3);
        TreeNode node06 = new TreeNode(6);
        TreeNode node07 = new TreeNode(9);
        node01.left = node02;
        node01.right = node03;

        node02.left = node04;
        node02.right = node05;

        node03.left = node06;
        node03.right = node07;

        printTree(node01);

        TreeNode root = mirrorTree(node01);
        printTree(root);

    }
}
