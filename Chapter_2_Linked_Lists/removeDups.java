/* Remove Dups
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP: How would you solve this problem if a temporary buffer was not allowed?

If I were to solve it optimizing time, then I would use a HashSet because it has 
constant insertion, deletion, and lookup which is useful for checking whether a
duplicate exists in the linked list. If I were to optimize space, then I would
use a runner implementation in order to check for duplicates in place, without
needing to use an external data structure.

Current Solution
Time Complexity: O(n) where n is the length of the linked list.
Space Complexity: O(n) where n is the number of unique node data.  
*/

import java.util.*; // just for hash set

public class removeDups {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insert(10);
        list.insert(8);
        list.insert(10);
        list.insert(4);
        list.insert(2);
        list.insert(123);
        list.insert(2);
        list.show();
        System.out.println("Before");
        removeDuplicates(list);
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
        removeDuplicates(list);
        list.show();
        System.out.println("After");

    }

    static void removeDuplicates(LinkedList list) {
        HashSet<Integer> set = new HashSet<Integer>();
        // set the head node to n so that I can iterate through it
        Node n = list.head;
        // add the first node's data to the set
        set.add(n.data);

        while (n.next != null) { // while there exists a node after this current one
            /*
             * if the set contains the next node's data, then i know i need to skip the next
             * node.
             */
            if (set.contains(n.next.data)) {
                n.next = n.next.next; // this line does the actual skipping
            } else { // if the set does not contain the next node's data, then add it to set.
                set.add(n.next.data);
                n = n.next;
            }
        }
    }
}
