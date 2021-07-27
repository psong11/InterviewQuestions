/* Remove Duplicate Node
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

Current Solution
Time Complexity: O(1)
Space Complexity: o(1)
*/

public class deleteMiddle {

    // Copy over next node's information and then "delete" next node.
    static void deleteMiddleMethod(Node middleNode) {
        if (middleNode.next == null) {
            System.out.println("Failed to delete. Not middle node.");
            return;
        } else {
            middleNode.data = middleNode.next.data;
            middleNode.next = middleNode.next.next;
        }
    }
}
