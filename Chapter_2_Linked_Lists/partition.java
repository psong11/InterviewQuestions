/* Partition
Write code to partition a linked list around a value x, 
such that all nodes less than x come before all nodes 
greater than or equal to x. If x is contained within 
the list, the values of x only need to be after the elements
less than x (see below).

input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (partition = 5)
output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


Current Solution
Time Complexity:
Space Complexity: 
*/

public class partition {
    static void partitionMethod(LinkedList list, int pivot) {
        // Create three different linked lists that contain
        // the numbers before, equal to, and after the pivot.
        // Merge at the end.
        Node beforePivotHead = null, beforePivotTail = null;
        Node afterPivotHead = null, afterPivotTail = null;
        Node equalPivotHead = null;

        Node n = list.head;
        while (n.next != null) {
            if (n.data < pivot) {
                if (beforePivotHead == null) {
                    beforePivotHead = n;
                    beforePivotTail = n;
                } else {
                    beforePivotTail.next = n;
                }
            }
            n = n.next;
        }

    }
}
