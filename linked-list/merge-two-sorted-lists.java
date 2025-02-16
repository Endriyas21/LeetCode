/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0); // Initialize dummy node
        ListNode curr = dummy; // Initialize current pointer to dummy node

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                curr.next = list1; // Point to list1 node
                list1 = list1.next; // Move list1 pointer
            } else {
                curr.next = list2; // Point to list2 node
                list2 = list2.next; // Move list2 pointer
            }
            curr = curr.next; // Move current pointer
        }

        // Attach the remaining part of list1 or list2
        if (list1 != null) {
            curr.next = list1;
        } else if (list2 != null) {
            curr.next = list2;
        }

        return dummy.next; // Return the merged list starting from the next node of dummy
    }
}