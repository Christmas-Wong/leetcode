public class main {

    /**
     * Definition for singly-linked list.
     */
    static class ListNode {
          int val;
          ListNode next;
          ListNode(int x) {
              val = x;
              next = null;
          }
      }
    public static ListNode detectCycle(ListNode head) {
        if (head==null || head.next==null || head.next.next==null){
            return null;
        }
        ListNode secondNode = head.next;
        ListNode thirdNode = head.next.next;
        while (secondNode!=null && thirdNode!=null){
            if (secondNode == thirdNode){
                ListNode forthNode = head;
                while(secondNode!=null && forthNode!=null){
                    if (secondNode==forthNode){
                        return secondNode;
                    }
                    secondNode = secondNode.next;
                    forthNode = forthNode.next;
                }
            }
            if (secondNode.next == null){
                return null;
            }else{
                secondNode = secondNode.next;
            }
            if (thirdNode.next=null || thirdNode.next.next == null){
                return null;
            }else{
                thirdNode = thirdNode.next.next;
            }
        }
        return null;

    }

    public static void main(String[] args) {
        ListNode node01 = new ListNode(3);
        ListNode node02 = new ListNode(2);
        ListNode node03 = new ListNode(0);
        ListNode node04 = new ListNode(-4);

        node01.next = node02;
//        node02.next = node01;
        node02.next= node03;
        node03.next= node04;
//        node04.next= node02;

        ListNode pointNode = detectCycle(node01);
        if (pointNode==null){
            System.out.println("Null value");
        }else{
            System.out.println(pointNode.val);
        }


    }
}
