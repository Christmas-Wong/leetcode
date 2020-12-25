import java.util.*;

/**
 * @Author Wang Fei
 * @Date 2020/12/3 15:51
 * @Version 1.0
 */
public class main {
    class Node {
        int val;
        Node next;
        Node random;

        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }

    public Node copyRandomList(Node head){
        if (head == null){
            return null;
        }
        Map<Node, Node> nodes = new HashMap<>();
        Node point = head;
        while (point != null){
            Node newNode = new Node(point.val);
            nodes.put(point, newNode);
            point = point.next;
        }
        point = head;
        while (point != null){
            nodes.get(point).next = nodes.get(point.next);
            if (point.random != null){
                nodes.get(point).random = nodes.get(point.random);
            }
            point = point.next;
        }
        return nodes.get(head);
    }

    public static void main(String[] args) {
        String originString = "pw";
        System.out.println(originString);

    }
}
