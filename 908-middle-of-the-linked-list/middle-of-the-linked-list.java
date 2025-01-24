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
    public ListNode middleNode(ListNode head) {
    //     int count = 0;

    //     ArrayList<ListNode> nodeList = new ArrayList<>();

    //     while (head != null) {
    //         count++;
    //         nodeList.add(head);
    //         head = head.next;
    //     }

    //     return nodeList.get(count / 2);
    // }

        ListNode middle = head;
        ListNode end = head;

        while (end != null && end.next != null) {
            middle = middle.next;
            end = end.next.next;
        }

        return middle;
    }
}