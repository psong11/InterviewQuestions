public class Main {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        System.out.println("Testing Remove Duplicates");
        list.insert(10);
        list.insert(8);
        list.insert(10);
        list.insert(4);
        list.insert(2);
        list.insert(123);
        list.insert(2);
        list.show();
        System.out.println("Before");
        removeDups.removeDupsMethod(list);
        list.show();
        System.out.println("After");
        list.clear();

        list.insert(1);
        list.insert(2);
        list.insert(2);
        list.insert(2);
        list.insert(5);
        list.insert(6);
        list.insert(7);
        list.show();
        System.out.println("Before");
        removeDups.removeDupsMethod(list);
        list.show();
        System.out.println("After");
        list.clear();

        System.out.println("Testing Return Kth");
        list.insert(1);
        list.insert(4);
        list.insert(3);
        list.insert(6);
        list.insert(8);
        list.insert(7);
        list.show();
        System.out.println("length: " + list.length());
        System.out.println("2nd to last: " + returnKthToLast.returnKthToLastMethod(list, 2));
        list.clear();

        System.out.println("Testing Delete Middle Node");
        list.insert(1);
        list.insert(2);
        list.insert(3);
        list.insert(4);
        list.insert(5);
        list.show();
        System.out.println("Deleting middle node...");
        deleteMiddle.deleteMiddleMethod(list.head.next.next);
        list.show();
        list.clear();
    }
}
