public class LinkedList {
    Node head;

    public void insert(int data) {
        Node node = new Node(data);
        if (head == null) {
            head = node;
        } else {
            Node n = head;
            while (n.next != null) {
                n = n.next;
            }
            n.next = node;
        }
    }

    public void delete(int data) {
        Node n = head;
        if (n.data == data) {
            head = head.next;
        }
        while (n.next != null) {
            if (n.next.data == data) {
                n.next = n.next.next;
                break;
            } else {
                n = n.next;
            }
        }
    }

    public void clear() {
        head = null;
    }

    public void show() {
        Node n = head;
        while (n.next != null) {
            System.out.println(n.data);
            n = n.next;
        }
        System.out.println(n.data);
    }
}
