/* Return Kth to Last
Implement an algorithm to find the kth to last element of a singly linked list.

Current Solution
Time Complexity: O(n) where n is the length of the linked list. 
Space Complexity: O(n) where n is the length of the linked list. Hashmap needs to store 
every value with its index.
*/

import java.util.*;

public class returnKthToLast {
    static int returnKthToLastMethod(LinkedList list, int k) {
        Node n = list.head;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int i = 0;
        while (n.next != null) {
            map.put(i, n.data);
            i++;
            n = n.next;
        }
        return map.get(list.length() - k - 1);
    }
}
