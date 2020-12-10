import com.sun.deploy.util.StringUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Author Wang Fei
 * @Date 2020/12/3 15:51
 * @Version 1.0
 */
public class main {

    /**
     * Definition for singly-linked list.
     */
      public static class ListNode {
          int val;
          ListNode next;
          ListNode(int x) { val = x; }
      }
    public static ListNode reverseList(ListNode head) {
        if (head == null){
            return null;
        }
        List<ListNode> returnList = new ArrayList<>();
        while (head !=null){
            returnList.add(head);
            head = head.next;
        }
        int length = returnList.size();
        for (int i = 0;i<length-1;i++){
            returnList.get(length-1-i).next = returnList.get(length-1-i-1);
        }
        returnList.get(0).next = null;
        return returnList.get(length-1);
    }

    public static ListNode doublePointer(ListNode head){
        if (head == null){
            return null;
        }
        ListNode cur = null;
        ListNode next = head;
        while (next!=null){
            ListNode t = next.next;
            next.next = cur;
            cur = next;
            next = t;
        }
        return cur;
    }

    public static ListNode recursion(ListNode head){
        if (head == null || head.next == null) {
            return head;
        }
        ListNode ret = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return ret;
    }

    public static void main(String[] args) {
        ListNode node01 = new ListNode(1);
        ListNode node02 = new ListNode(2);
        ListNode node03 = new ListNode(3);
        ListNode node04 = new ListNode(4);
        ListNode node05 = new ListNode(5);

        node01.next = node02;
        node02.next = node03;
        node03.next = node04;
        node04.next = node05;

        ListNode returnNode = recursion(node01);
        while (returnNode!=null){
            System.out.println(returnNode.val);
            returnNode = returnNode.next;
        }
    }

}
