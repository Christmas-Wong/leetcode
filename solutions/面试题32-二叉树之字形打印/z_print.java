
import java.util.*;

public class main {
    static class TreeNode{
        private int val;
        private TreeNode left = null;
        private TreeNode right = null;
        TreeNode(int x){
            this.val = x;
        }
    }

    public static List<List<Integer>> binary_tree_z_print(TreeNode head){
        if (head == null){
            return new ArrayList<>();
        }
        Stack<TreeNode> stack_odd = new Stack<>();
        Stack<TreeNode> stack_even = new Stack<>();
        stack_odd.push(head);
        List<List<Integer>> returnList = new ArrayList();
        int counter = 0;
        int index = 0;
        List<Integer> eleList = new ArrayList();
        while (stack_odd.size()>0 || stack_even.size()>0){
            if (stack_odd.size()>0 && counter%2==0){
                TreeNode node = stack_odd.pop();
                eleList.add(node.val);
                if (node.left != null){
                    stack_even.push(node.left);
                }
                if (node.right != null){
                    stack_even.push(node.right);
                }
                if (stack_odd.size()<=0){
                    counter++;
                    returnList.add(new ArrayList<>(eleList));
                    eleList.clear();
                }
                continue;
            }
            if (stack_even.size()>0 && counter%2==1){
                TreeNode node = stack_even.pop();
                eleList.add(node.val);
                if (node.right != null){
                    stack_odd.push(node.right);
                }
                if (node.left != null){
                    stack_odd.push(node.left);
                }
                if (stack_even.size()<=0){
                    counter++;
                    returnList.add(new ArrayList<>(eleList));
                    eleList.clear();
                }
                continue;
            }
        }
        return returnList;

    }


    public static void main(String[] args){
        TreeNode node01 = new TreeNode(1);
        TreeNode node02 = new TreeNode(2);
        TreeNode node03 = new TreeNode(3);
        TreeNode node04 = new TreeNode(4);
        TreeNode node05 = new TreeNode(5);
        TreeNode node06 = new TreeNode(6);
        TreeNode node07 = new TreeNode(7);

        node01.left = node02;
        node01.right = node03;
        node02.left = node04;
        node03.left = node06;
        node03.right = node05;
        System.out.println(binary_tree_z_print(node01));;
    }
}
